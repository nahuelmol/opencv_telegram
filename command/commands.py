from telegram import Update
from telegram.ext import CallbackContext

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)



def method_example(update:Update,context:CallbackContext):
	mylist = context.args
	text = "Hola"
	print(type(mylist))
	print(mylist)
	update.message.reply_text(f'{text}')
	

def start(update, context):
    context.bot.send_message(
    	chat_id=update.effective_chat.id, 
    	text="I'm a bot, please talk to me!"
    	)

class Sender:
	def __init__(self,bot):
		self.bot = bot

	def image_send(self,update:Update,context:CallbackContext):
		mylist = context.args

		self.bot.send_photo(
			chat_id=update.effective_chat.id, 
			photo=open('test/{}.jpg'.format(mylist[0]), 'rb'))

