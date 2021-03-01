import os 

from telegram.ext import Updater, CommandHandler
from telegram import Bot

from dotenv import load_dotenv
from pathlib import Path

from command.commands import method_example, start
from command.commands import Sender

load_dotenv(verbose=True)

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)

token = os.getenv("bot-token")

updater = Updater(token, use_context=True)
dispatcher = updater.dispatcher

bot = Bot(token)

init = CommandHandler('example', method_example, pass_args=True,pass_chat_data=True)
start_handler = CommandHandler('start', start)
image_sender = CommandHandler('sendme', Sender(bot).image_send,pass_args=True, pass_chat_data=True)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(init)
dispatcher.add_handler(image_sender)

updater.start_polling()
updater.idle()