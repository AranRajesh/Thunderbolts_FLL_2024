from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, Light, ColorLightMatrix
from pybricks.parameters import Port, Direction, Color, Stop
from pybricks.geometry import Axis
from pybricks.robotics import DriveBase,
from pybricks.tools import wait, StopWatch
from pybricks.pupdevices import ColorSensor
hub = PrimeHub()
# Initialize the timer
timer = StopWatch()
timer.reset()


# Initialize both motors. In this example, the motor on the
# left must turn counterclockwise to make the robot go forward.
left_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.B)
# Initialize the color sensors

right_sensor = ColorSensor(Port.F)
left_sensor = ColorSensor(Port.E)

# Initialize the arm motors
right_arm_motor = Motor(Port.D)
left_arm_motor = Motor(Port.C)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
bot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)

bot.straight(250)
bot.turn(50)
bot.straight(140)
bot.turn(-50)
bot.straight(320)
bot.turn(-70)
bot.straight(150)
