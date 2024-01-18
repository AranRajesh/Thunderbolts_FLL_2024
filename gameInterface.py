from primeBot import primeBot
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Button

class gameInterface:

    def __init__(self, bot: primeBot, shut_down_after:int = 30) -> None:
        self.runs = []
        self.bot = bot
        self.shut_down_after = shut_down_after
        self.current_run = 1
        self.timer_all = StopWatch()
        self.timer_run = StopWatch()
        self.timer_shutdown = StopWatch()
        self.first_run_initiated = False
        self.start = self._main

        # Configure the stop button combination. Now, your program stops
        # if you press the center and Bluetooth buttons simultaneously.
        self.bot.hub.system.set_stop_button((Button.LEFT, Button.RIGHT))
    
    def addRun(self, func):
        self.runs.append(func)
    

    # --------------------------------------------------------------------------------
    # cycle to the next run
    def nextRun(self):
    # --------------------------------------------------------------------------------
        N_RUNS = len(self.runs)
        self.current_run = (self.current_run+1) if self.current_run<N_RUNS else 1
    # --------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------
    # cycle to the previous run
    def previousRun(self):
    # --------------------------------------------------------------------------------
        N_RUNS = len(self.runs)
        self.current_run = (self.current_run-1) if self.current_run>1 else N_RUNS
    # --------------------------------------------------------------------------------

    # --------------------------------------------------------------------------------
    # Main program loop
    # --------------------------------------------------------------------------------
    # Intialize bot, wait for button press and launch runs
    def _main(self):
        self.bot.hub.display.char(f"{self.current_run}")
        self.timer_shutdown.reset()
        while (self.timer_shutdown.time() < self.shut_down_after*1000*60):
            pressed = []
            while not any([pressed]):
                pressed = self.bot.hub.buttons.pressed()
                wait(10)
            # Wait for all buttons to be released. 
            while any (self.bot.hub.buttons.pressed()):
                wait (10)
            
            if Button.LEFT in pressed:
                self.previousRun()
            elif Button.RIGHT in pressed:
                self.nextRun()
            elif Button.CENTER in pressed:
                if (not self.first_run_initiated):
                    self.first_run_initiated = True
                    self.timer_all.reset()
                print (f"Run {self.current_run} started, overall Time: {self.timer_all.time()/1000} s")
                self.timer_run.reset()           
                self.bot.reset_DriveBase()
                self.runs[self.current_run-1](self.bot)
                self.bot.play_notes(["C4/16"])
                print (f"Run {self.current_run} completed in {self.timer_run.time()/1000} s")
                print (f"Overall Time: {self.timer_all.time()/1000} s")
                self.bot.reset_DriveBase()
                self.nextRun()
            elif Button.BLUETOOTH in pressed:
                if (self.current_run==3):
                    pass    
                    # selectNumSceneChange()
                
            self.bot.hub.display.char(f"{self.current_run}")
            print (f"Run {self.current_run} selected")

            wait(50)



                        


