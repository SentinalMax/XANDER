from chatterbot import ChatBot
#from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'XANDER',  
    logic_adapters=[
       
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',]
    )

#trainer = ListTrainer(bot)
trainer = ChatterBotCorpusTrainer(bot)

name=input("Enter Your Name: ")

trainer.train([
    "chatterbot.corpus.english"
])

print("Hello, " + name + ". I am XANDER; say 'bye' to exit.")
while True:
    request=input(name+':')

    if request=='Bye' or request =='bye':
        print('XANDER: Goodbye')
        break
    else:
        response=bot.get_response(request)
        print('Zander:',response)