from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_wheel= Motor(Port.A,Direction.COUNTERCLOCKWISE)
right_wheel= Motor(Port.B)
bot = DriveBase(left_wheel,right_wheel,56,80)
bot.settings(straight_speed=600,straight_acceleration=600)
bot.straight(-500)
bot.straight(200)

