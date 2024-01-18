from primeBot import primeBot
from pybricks.tools import wait, StopWatch

###############################################
## Write your code in this function 
## Note you can rename this if you want 
#----------------------------------------------

def vrArtist(bot: primeBot):
    bot.straight(150)
    bot.turn(-45)
    bot.drive(400, 0)
    wait(2000)
    bot.stop()
    bot.left_arm_motor.run_angle(5000,-3700)
    bot.right_arm_motor.run_angle(500, -550)
    bot.drive(-700,5)
    wait(2000)
    bot.stop()
    # For the code to work, the alignment has to be 20 from right home area!
    return


if __name__ == "__main__": 
    missionFunction = vrArtist
# ----------------------------------------------
###############################################
## You don't need to modify anything  below this line

    timer = StopWatch()
    myBot = primeBot()
    missionFunction(myBot)
    print(f"Completed in {timer.time()/1000} s")
