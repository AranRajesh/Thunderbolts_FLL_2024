from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, Light, ColorLightMatrix
from pybricks.parameters import Port, Direction, Color, Stop
from pybricks.geometry import Axis
from pybricks.robotics import DriveBase
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


print (bot.settings())
bot.settings(300, 300, 100, 100)
# Drive Until Stalled function:
def drive_straight_until_stalled(speed = 600):
    bot.drive(speed,0)
    while (not bot.stalled()):
         wait(100)
    bot.stop()


# Optionally, uncomment the line below to use the gyro for improved accuracy.
bot.use_gyro(True)
print('Initialized Bot')
bot.straight(150)
bot.turn(-55)
drive_straight_until_stalled(400)
left_arm_motor.run_angle(5000,3700)
right_arm_motor.run_angle(500, -550)
bot.straight(-430)
bot.turn(50)

# For the code to work, the alignment has to be 20 from right home area!
# It's completed! Note: This was coded on the second table!