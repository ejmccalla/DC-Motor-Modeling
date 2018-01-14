import sys
from scipy import signal
import numpy as np
from matplotlib import pyplot as plt
from state_space_model_inputs import *

# ------------------------------------------------------------------------------
# DC Motor Equations
#
# V = input voltage, T = input load torque
# i = ouput current, w = output rotational velocity
# R = Winding resistance, Kv = Voltage constant, L = Winding inductance
# F = Viscous damping, Kt = Torque coefficient, J = Rotor moment-of-inertia
#
# V = R*i + Kv*w + L*di/dt
# T = Kt*i - F*w -J*dw/dt
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# DC Motor Coefficients
if Motor_Type == 'CIM':
    R = 0.09156461028
    Kv = 0.0210564841
    L = 0.000059
    F = 0.00008905383993
    Kt = 0.01841211705
    J = 0.0000775
else:
    print ('Unsupported motor-type %s' % (Motor_Type))
    sys.exit()

# ------------------------------------------------------------------------------
# State-Space Representation
#
#               _______A_______   __X__   ______B______   __U__
#               |             |   |   |   |           |   |   |
#       -- --   --           --   -- --   --         --   -- --
#   d   | i |   | -R/L  -Kv/L |   | i |   | 1/L    0  |   | V |
#  -- * |   | = |             | * |   | + |           | * |   |
#  dt   | w |   | Kt/J   -F/J |   | w |   |  0   -1/J |   | T |
#       -- --   --           --   -- --   --         --   -- --
#
#           ____C___   __X__   ___D____   __U__
#           |      |   |   |   |      |   |   |
#  --  --   --    --   -- --   --    --   -- --
#  | y1 |   | 1  0 |   | i |   | 0  0 |   | V |
#  |    | = |      | * |   | + |      | * |   |
#  | y2 |   | 0  1 |   | w |   | 0  0 |   | T |
#  --  --   --    --   -- --   --    --   -- --
#

# ------------------------------------------------------------------------------
# These values are constant for all keys of the robot inputs.
#   T   :  This is an array of time value simulation inputs
#   Vi  :  This is an array of voltage simulation inputs
#   C   :  This is the C-matrix for the SS model
#   D   :  This is the D-matrix for the SS model
T = np.linspace(0, Simulation_Time, Simulation_Time / SampleRate)
Vi = 12*np.ones(len(T))
C = [[1, 0], [0, 1]]
D = [[0, 0], [0, 0]]

# ------------------------------------------------------------------------------
# Create objects in preperation for plotting the modeling output.
fig = plt.figure()
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

# ------------------------------------------------------------------------------
# Loop over all of the robot input configurations.
#   Jl       : This is the load plus rotor moment-of-inertia
#   A        : This is the A-matrix for the SS model
#   B        : This is the B-matrix for the SS model
#   SS_Model : This is the state-space model
#   Tl       : This is an array of load torque simulation inputs
#   U        : This is the input matrix for the simulation

for key in Robot_Inputs:
    Jl = J + Robot_Inputs[key][1]
    A = [[-1.0*R/L, -1.0*Kv/L], [Kt/Jl, -1.0*F/Jl]]
    B = [[1/L, 0], [0, -1.0/Jl]]
    SS_Model = signal.StateSpace(A, B, C, D)
    Tl = Robot_Inputs[key][0]*np.ones(len(T))
    U = np.transpose(np.array([Vi, Tl]))

    t1, y1, x1 = signal.lsim(SS_Model, U, T)

    ax1.plot(t1, (60.0*np.transpose(y1)[1])/(2.0*np.pi), label=key)
    ax2.plot(t1, np.transpose(y1)[0], label=key)
    print ('%s,%3.1f,%i' % (key, np.transpose(y1)[0][-1],
                            (60.0*np.transpose(y1)[1][-1]) / (2.0*np.pi)))


# ------------------------------------------------------------------------------
# Plot the simulation results
ax1.set_ylabel('Rotational Velocity (RPM)')
ax2.set_ylabel('Current (A)')
ax2.set_xlabel('Time (s)')
ax1.legend(bbox_to_anchor=(1, 1.04), loc='upper left')
plt.subplots_adjust(right=0.6)
ax1.grid()
ax2.grid()
plt.show()
