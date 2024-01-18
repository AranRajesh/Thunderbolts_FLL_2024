from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
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
right_arm_motor = Motor(Port.C)
left_arm_motor = Motor(Port.D)

# Initialize the drive base. In this example, the wheel diameter is 56mm.
# The distance between the two wheel-ground contact points is 112mm.
bot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=80)


print (bot.settings())
bot.settings(300, 300, 233, 300)

# Optionally, uncomment the line below to use the gyro for improved accuracy.
bot.use_gyro(True)
print('Initialized Bot')
bot.straight(100)
bot.turn(15)
bot.straight(150)
bot.turn(5)
bot.straight(280)
bot.straight(40)
bot.straight(40)
bot.straight(50)
bot.straight(40)
bot.turn(50)
bot.turn(30)
bot.turn(-5)
bot.straight(600)
