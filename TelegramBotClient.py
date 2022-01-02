import logging
import string
from threading import Thread
from typing import Callable

from telegram import Update
from telegram.ext import CallbackContext, CommandHandler, Updater
from telegram.ext.dispatcher import Dispatcher

from config import BOT_TOKEN
from storage.chatBotStorage import ChatBotStorage
from storage.tables import ChatBot


class TelegramBotClient:
    updater: Updater
    started: bool = False
    join_function: Callable[[str], None]

    def set_join_function(self, join_function: Callable[[str], None]):
        self.join_function = join_function


    def start(self):
        if not self.started:
            Thread(target=self.__do_start__, args=(), daemon=True).start()

    def __do_start__(self):
        self.updater = Updater(token=BOT_TOKEN, use_context=True)
        dispatcher: Dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.__start_cmd__)
        dispatcher.add_handler(start_handler)

        filter_handler = CommandHandler('filter', self.__filter_cmd__)
        dispatcher.add_handler(filter_handler)

        join_handler = CommandHandler('join', self.__join_cmd__)
        dispatcher.add_handler(join_handler)

        self.updater.start_polling()

    def __start_cmd__(self, update: Update, context: CallbackContext):
        try:
            if update.effective_chat is None:
                raise Exception('Chat id or message is None')
            chat_id = update.effective_chat.id
            ChatBotStorage().insert(ChatBot(chat_id=chat_id, is_active=True))
            context.bot.send_message(chat_id=chat_id, text="Use /filter REGEX to filter content")
        except Exception as e:
            logging.error(e)

    def __join_cmd__(self, update: Update, context: CallbackContext):
        try:
            if update.effective_chat is None or update.message is None or update.message.text is None:
                raise Exception('Chat id or message is None')
            chat_id = update.effective_chat.id
            channel = update.message.text[6:]
            self.join_function(channel)
            storage = ChatBotStorage()
            chat = storage.get_by_chat_id(chat_id)
            new_channels = (chat.channels or '') + f' {channel}' if channel not in (chat.channels or '') else chat.channels
            setattr(chat, 'channels', new_channels)
            storage.insert(chat)
            context.bot.send_message(chat_id=chat_id, text="Use /join REGEX to filter content")
        except Exception as e:
            logging.error(e)

    def __filter_cmd__(self, update: Update, context: CallbackContext):
        try:
            if update.effective_chat is None or update.message is None or update.message.text is None:
                raise Exception('Chat id or message is None')
            chat_id: int = update.effective_chat.id
            filter_regex = update.message.text[8:]
            storage = ChatBotStorage()
            chat = storage.get_by_chat_id(chat_id)
            setattr(chat, 'filter', filter_regex)
            storage.insert(chat)
            context.bot.send_message(chat_id=chat_id, text=filter_regex)
        except Exception as e:
            logging.error(e)

    def send_message(self, chat_id: int, message: string):
        self.updater.bot.send_message(chat_id=chat_id, text=message)
