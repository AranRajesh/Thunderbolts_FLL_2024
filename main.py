from primeBot import primeBot
from gameInterface import gameInterface
from masterpiece import masterpiece

myBot = primeBot()
myBot.interface = gameInterface(bot=myBot)

myBot.interface.addRun(masterpiece)
myBot.interface.start()
