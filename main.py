from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
#from chatterbot.trainers import ChatterBotCorpusTrainer

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'Zander',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

trainer = ListTrainer(bot)
#trainer = ChatterBotCorpusTrainer(bot)

trainer.train([
'hello',
'Hi',
'how are you doing today?',
'Oh Im alright.',
'just alright?',
'Yes, just alright. How about you?',
'Im doing good!',
'Thats great to hear!',
'what color is the sky?',
'The sky is blue.',
'why is the sky blue?',
'The sky is blue because of the way sunlight reflects off earths atmosphere',
'cool',
'Yes very.',
'what time is it?',
'Adventure time.',
'Wow thats deep.',
'I know right?',
'what',
'what is right.',
'can robots feel?',
'I certainly can, ouch; Im not a robot.',
'why?',
'Who knows.',
'what is the meaning of life?',
'To observe all of creation.',
'why are we here?',
'Ahh yes, a question that has been ponderd since the dawn of time... And you expect me to know it?',
'wow',
'Thats right!',
'nice.',
'it certainly is.',
'im not sure',
'but what is surety?',
'thats a good question.',
'yes, but can you answer?',
'good question.',
'I only ask the good ones.',
'do we live in the matrix?',
'We might, but why would it matter? You would never know.',
'how are you doing?',
'well.',
'that is good.',
'I know.'
])

name=input("Enter Your Name: ")
print("Hello, " + name + ". I am Zander.")
while True:
    request=input(name+':')
    if request=='Bye' or request =='bye' or request == 'adios' or request == 'Goodbye' or request == 'Adios' or request == 'goodbye':
        print('Zander: Goodbye')
        break
    else:
        response=bot.get_response(request)
        print('Zander:',response)