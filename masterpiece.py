from primeBot import primeBot
from pybricks.tools import wait, StopWatch

###############################################
## Write your code in this function 
## Note you can rename this if you want 
#----------------------------------------------

def masterpiece(bot: primeBot):
    bot.straight(-130)
    bot.curve(-100,-80)
    bot.straight(-350)
    bot.turn(-20)
    bot.turn(-20)
    bot.straight(-410)
    bot.turn(-15)
    bot.straight(-150)
    bot.straight(400)
    bot.turn(-25)
    bot.drive(-230,0)
    wait(2500)
    bot.stop()


if __name__ == "__main__": 
    missionFunction = masterpiece
# ----------------------------------------------
###############################################
## You don't need to modify anything  below this line

    timer = StopWatch()
    myBot = primeBot()
    missionFunction(myBot)
    print(f"completed in {timer.time()/1000} s")

