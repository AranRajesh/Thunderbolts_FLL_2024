from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
leftWheelMotor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
rightWheelMotor = Motor(Port.B)
bot = DriveBase(leftWheelMotor,rightWheelMotor,wheel_diameter=56, axle_track=80)
bot.settings(300,300, 233, 300)
bot.use_gyro(True)
# Initialize Arm Motors
rightArmMotor = Motor(Port.D, Direction.CLOCKWISE)
leftArmMotor = Motor(Port.C, Direction.CLOCKWISE, [12,36])

def theaterSceneChange():
    bot.curve(1200,35)
    bot.turn(-60)
    rightArmMotor.run_angle(500,150)
    bot.straight(100)
    rightArmMotor.run_angle(500,-150)
    bot.straight(-60) 
    bot.turn(70)
    bot.drive(-600,2)
    wait(2000) 
    bot.stop() 
    bot.straight(-340)
theaterSceneChange()
