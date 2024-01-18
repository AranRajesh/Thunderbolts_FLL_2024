from primeBot import primeBot
from pybricks.tools import wait, StopWatch

###############################################
## Write your code in this function 
## Note you can rename this if you want 
#----------------------------------------------

def myMission(bot: primeBot):
    # bot.straight(100)
    # bot.drive(-600)
    # wait (500)
    # bot.stop()
    return


if __name__ == "__main__": 
    missionFunction = myMission
# ----------------------------------------------
###############################################
## You don't need to modify anything  below this line

    timer = StopWatch()
    myBot = primeBot()
    missionFunction()
    print(f"completed in {timer.time()/1000} s")