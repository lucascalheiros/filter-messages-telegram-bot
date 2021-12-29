import string
from threading import Thread

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater

from config import BOT_TOKEN
from storage.chatBotStorage import ChatBotStorage
from storage.tables import ChatBot


class TelegramBotClient:

    def __init__(self) -> None:
        self.started = False

    def start(self):
        if not self.started:
            Thread(target=self.__do_start__, args=(), daemon=True).start()

    def __do_start__(self):
        self.updater = Updater(token=BOT_TOKEN, use_context=True)
        dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.__start_cmd__)
        dispatcher.add_handler(start_handler)

        filter_handler = CommandHandler('filter', self.__filter_cmd__)
        dispatcher.add_handler(filter_handler)

        self.updater.start_polling()

    def __start_cmd__(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        context.bot.send_message(chat_id=chat_id, text="Use /filter REGEX to filter content")

    def __filter_cmd__(self, update: Update, context: CallbackContext):
        chat_id = update.effective_chat.id
        filter_regex = update.message.text[8:]
        ChatBotStorage().insert(ChatBot(chat_id=chat_id, is_active=True, filter=filter_regex))
        context.bot.send_message(chat_id=chat_id, text=filter_regex)

    def send_message(self, chat_id: int, message: string):
        self.updater.bot.send_message(chat_id=chat_id, text=message)
