from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create object of ChatBot class with Logic Adapter
bot = ChatBot(
    'Zander',  
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.TimeLogicAdapter'],
)

trainer = ListTrainer(bot)

trainer.train([
'Hi',
'Hello',
'I need your assistance regarding my order',
'Please, Provide me with your order id',
'I have a complaint.',
'Please elaborate, your concern',
'How long it will take to receive an order ?',
'An order takes 3-5 Business days to get delivered.',
'Okay Thanks',
'No Problem! Have a Good Day!'
])

# Get a response to the input text 'I would like to book a flight.'
response = bot.get_response('I have a complaint.')

print("Bot Response:", response)