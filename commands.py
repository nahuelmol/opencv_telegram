from telegram import Update
from telegram.ext import CallbackContext

def method_example(update:Update,context:CallbackContext):
	
	text = "Hola"

	update.message.reply_text(f'Translated text: {text}')