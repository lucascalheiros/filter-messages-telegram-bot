import string
from threading import Thread

from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from telegram.ext import Updater

import config
from storage.chatBotStorage import ChatBotStorage
from storage.tables import ChatBot


class TelegramBotClient:

    def __init__(self, chat_bot_storage: ChatBotStorage) -> None:
        self.started = False
        self.chat_bot_storage = chat_bot_storage

    def start(self):
        if not self.started:
            Thread(target=self.__do_start, args=(), daemon=True).start()

    def __do_start(self):
        self.updater = Updater(token=config.BOT_TOKEN, use_context=True)
        dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.__start)
        dispatcher.add_handler(start_handler)

        filter_handler = CommandHandler('filter', self.__filter)
        dispatcher.add_handler(filter_handler)

        # echo_handler = MessageHandler(Filters.text & (~Filters.command), self.__echo)
        # dispatcher.add_handler(echo_handler)

        self.updater.start_polling()

    def __start(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text="Use /filter REGEX to filter content")

    def __filter(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        filter_regex = update.message.text[8:]
        ChatBotStorage().insert(ChatBot(chat_id=chat_id, is_active=True, filter=filter_regex))
        context.bot.send_message(chat_id=chat_id, text=filter_regex)

    def __echo(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text=update.message.text)

    def send_message(self, chat_id: int, message: string):
        self.updater.bot.send_message(chat_id=chat_id, text=message)
