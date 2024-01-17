from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor
from pybricks.parameters import Button, Color, Icon, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch


N_RUNS = 7
current_run = 0

# make the number of scene changes configurable here 
# to help coordinate with partner team and maximize bonus points
N_SCENE_CHANGES = 2

BLACK_REFLECTION_THRESHOLD = 20
WHITE_REFLECTION_THRESHOLD = 60

# ################################################################################
## Initialization Function
# --------------------------------------------------------------------------------

def init():
    global hub, left_wheel_motor, right_wheel_motor, bot, left_arm_motor,\
           right_arm_motor, left_color_sensor, right_color_sensor, timer_run, timer_all

    # Initialize the Hub
    hub = PrimeHub()

    # Initialize the hub with rainbow colors
    # hub.light.animate([Color(h=i * 8) for i in range(45)], interval=40)

    # Configure the stop button combination. Now, your program stops
    # if you press the center and Bluetooth buttons simultaneously.
    hub.system.set_stop_button((Button.LEFT, Button.RIGHT))

    # Initialize the wheel motors and use them to initalize the drivebase
    left_wheel_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
    right_wheel_motor = Motor(Port.B)
    bot = DriveBase(left_wheel_motor,right_wheel_motor,wheel_diameter=56, axle_track=80)
    reset_DriveBase()

    # Initialize Arm Motors
    right_arm_motor = Motor(Port.D, Direction.CLOCKWISE)
    left_arm_motor = Motor(Port.C, Direction.CLOCKWISE)

    # Initialize Color Sensors
    left_color_sensor = ColorSensor(Port.E)
    right_color_sensor = ColorSensor(Port.F)

    # Setup timers for individual runs and overall match
    timer_run = StopWatch()
    timer_run.reset()
    timer_all = StopWatch()
    timer_all.reset()
    print ('Init Complete!')
    print (f'Battery Level {hub.battery.voltage()}')

def reset_DriveBase():
    global bot
    
    hub.light.on(Color.ORANGE)          # Signal we are calibrating

    # Set speed and acceleration conservatively (half of default values)
    # we want to optimize for accuracy
    bot.settings(straight_speed=300, straight_acceleration=300, turn_rate=233, turn_acceleration=300)
    
    # Use gyro for all bot movements
    bot.use_gyro(True)

    # Reset drive base and gyro
    bot.reset()
    hub.imu.reset_heading(0)
    wait (200)

    # wait until Hub is calibrated and ready 
    while (not hub.imu.ready()):
        wait(50)
    hub.light.on(Color.GREEN)



init()

#=========================================================================================
# Write your code here:

