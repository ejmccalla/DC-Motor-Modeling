# ------------------------------------------------------------------------------
# Input the type of motor as a string value.
Motor_Type = 'CIM'

# ------------------------------------------------------------------------------
#
# THIS IS WHERE THE DATA COPIED FROM STEP 2 GOES
#
# Setup the robot input dictionary.  The key is a string which serves as a
# description of the configuration being modeled.  The tuple values are the
# Load Torque @ Motor and the Robot Moment of Intertia @ Motor.
Robot_Inputs = {
    '5.95':  (0.35658646, 0.00334776),
    '8.45':  (0.25108751, 0.00165987),
    '10.71': (0.19810359, 0.00103326),
    '12.75': (0.16640702, 0.00072907),
}

# ------------------------------------------------------------------------------
# Input the length of time, in seconds, to run the simulation as a
# floating-point value.
Simulation_Time = 5.0

# ------------------------------------------------------------------------------
# Input the sample rate, in seconds, to collect the simulation data.
SampleRate = 0.02
