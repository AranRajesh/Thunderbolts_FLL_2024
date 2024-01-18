from primeBot import primeBot
from pybricks.tools import wait

###############################################
## Write your code in this function 
## Note you can rename this if you want 
#----------------------------------------------

def test (bot: primeBot):
    bot.display("Hi!")
    bot.straight(100)
    bot.turn(60)


if __name__ == "__main__": 
    missionFunction = test
# ----------------------------------------------
###############################################
## You don't need to modify anything  below this line

    myBot = primeBot()
    missionFunction(myBot)
