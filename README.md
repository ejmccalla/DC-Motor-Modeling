This project contains the source needed to model the open-loop dynamics and
steady-state of a brushed DC motor.  The differential equations governing
the motor behavior are below.
# -------------------------------------------------------------------------
# DC Motor Equations
#
# V = input voltage, T = input load torque
# i = ouput current, w = output rotational velocity
# R = Winding resistance, Kv = Voltage constant, L = Winding inductance
# F = Viscous damping, Kt = Torque coefficient, J = Rotor moment-of-inertia
#
# V = R*i  + Kv*w + L*di/dt
# T = Kt*i - F*w  - J*dw/dt
# -------------------------------------------------------------------------

Using a state-space model to solve for the equations requires creating the
matrices below.  For further reading, refer to the following link:  
https://www.ee.usyd.edu.au/tutorials_online/matlab/examples/motor/motor.html
# -------------------------------------------------------------------------
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
# -------------------------------------------------------------------------

The state_space_model_inputs.py file is where the user can make changes to
the inputs of the model.  For a CIS 4607 team member, copy the 
"Gear Ratio", "Load Torque @ Motor (N·m)", and the 
"Moment of Inertia @ Motor Shaft (Kg·m²)" data from the Drivetrain Analysis
Google Sheets docuement.

Run state_space_model.py to run the model and generate a plot of the output
motor RPM's and current draw.  This data can be used to verify the modeling
of the steady-state values derived using kinematics, the time it take to
accelerate to full speed, the current draw over time, etc.
