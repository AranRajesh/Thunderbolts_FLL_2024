from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

class primeBot():

    shutdownNotes = ["C4/16", "R/16", "C3/16","R/16", "C2/16"]
    def __init__(self):
        self.hub = PrimeHub()
       
        # Initialize the wheel motors and use them to initalize the drivebase
        self.left_wheel_motor = Motor(Port.A, Direction.COUNTERCLOCKWISE)
        self.right_wheel_motor = Motor(Port.B)
        self.drive_base = DriveBase(self.left_wheel_motor,self.right_wheel_motor,wheel_diameter=56, axle_track=80)
        self.reset_DriveBase()

        # Initialize Arm Motors
        self.right_arm_motor = Motor(Port.D, Direction.CLOCKWISE)
        self.left_arm_motor = Motor(Port.C, Direction.CLOCKWISE)

        # Initialize Color Sensors
        self.left_color_sensor = ColorSensor(Port.E)
        self.right_color_sensor = ColorSensor(Port.F)

        
        # Copy interesting methods from member attributes to our class 
        # along with their documentation (for intellisense)
        self.heading = self.hub.imu.heading
        self.reset_heading = self.hub.imu.reset_heading
        self.display = self.hub.display.text
        self.play_notes = self.hub.speaker.play_notes
        self.straight = self.drive_base.straight
        self.stop = self.drive_base.stop
        self.drive = self.drive_base.drive
        self.turn = self.drive_base.turn
        self.curve = self.drive_base.curve
        
        print ('Init Complete!')
        print (f'Battery Level {self.hub.battery.voltage()}')



    def reset_DriveBase(self):
        self.hub.light.on(Color.ORANGE)          # Signal we are calibrating

        # Set speed and acceleration conservatively (half of default values)
        # we want to optimize for accuracy
        self.drive_base.settings(straight_speed=300, straight_acceleration=300, turn_rate=233, turn_acceleration=300)
        
        # Use gyro for all bot movements
        self.drive_base.use_gyro(True)

        # Reset drive base and gyro
        self.drive_base.reset()
        self.hub.imu.reset_heading(0)
        wait (200)

        # wait until Hub is calibrated and ready 
        while (not self.hub.imu.ready()):
            wait(50)
        self.hub.light.on(Color.GREEN)        
    

    def shutdown(self):
        print ("Shutting Down Robot!")
        self.play_notes(primeBot.shutdownNotes)
        self.hub.system.shutdown()


