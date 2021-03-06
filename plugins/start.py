from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.dispatcher import run_async

class Plugin:
    def __init__(self, main, updater):
        updater.dispatcher.add_handler(CommandHandler('start', self.start))

    @run_async
    def start(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Welcome")
