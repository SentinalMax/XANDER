import time
import random
import sys
from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

#variables
words = " "

#typing function
def faketype(words):
  words
  for char in words:
    time.sleep(random.choice([0.3, 0.11, 0.08, 0.07, 0.07, 0.07, 0.06, 0.06, 0.05, 0.01]))
    sys.stdout.write(char)
    sys.stdout.flush()
  time.sleep(1)

#Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'XANDER',  
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.20
        },
        ],
)

#trainer = ListTrainer(bot)
trainer = ChatterBotCorpusTrainer(bot)

trainer.train(
    "chatterbot.corpus.english"
)

name=input("Enter Your Name: ")

print("Hello, " + name + ". I am XANDER; say 'bye' to exit.")
while True:
    request=input('\n'+name+':\n')

    if request=='Bye' or request =='bye':
        print('XANDER: Goodbye')
        break
    else:
        print('XANDER: ')
        response=bot.get_response(request)
        string = str(response) #concat responses
        faketype(string)
        #print('XANDER:',response)

