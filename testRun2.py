from primeBot import primeBot
from pybricks.tools import wait, StopWatch

###############################################
## Write your code in this function 
## Note you can rename this if you want 
#----------------------------------------------

def run2(bot:primeBot):
    bot.play_notes(["C3/16", "C4/16", "C5/16"])

if __name__ == "__main__": 
    missionFunction = run2
# ----------------------------------------------
###############################################
## You don't need to modify anything  below this line

    timer = StopWatch()
    myBot = primeBot()
    missionFunction(myBot)
    print(f"completed in {timer.time()/1000} s")