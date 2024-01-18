from primeBot import primeBot
from gameInterface import gameInterface
from test_run1 import test
from testRun2 import run2

myBot = primeBot()
myBot.interface = gameInterface(bot=myBot)

myBot.interface.addRun(test)
myBot.interface.addRun(run2)
myBot.interface.start()
