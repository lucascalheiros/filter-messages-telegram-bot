from telegram.ext import Updater
import config
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from time import sleep
from threading import Thread


class TelegramBotClient():
    
    def __init__(self) -> None:
        self.started = False

    def startbot(self):
        if not self.started:
            Thread(target=self.__do_startbot, args=(), daemon=True).start()

    def __do_startbot(self):
        self.updater = Updater(token=config.BOT_TOKEN, use_context=True)
        dispatcher = self.updater.dispatcher

        start_handler = CommandHandler('start', self.__start)
        dispatcher.add_handler(start_handler)

        echo_handler = MessageHandler(Filters.text & (~Filters.command), self.__echo)
        dispatcher.add_handler(echo_handler)

        self.updater.start_polling()


    def __itermitant_message_sender(self, id):
        while (True):
            sleep(2)
            if not id is None:
                self.updater.bot.send_message(chat_id=id, text="test")
            print(id)

    def __start(update: Update, context: CallbackContext):
        context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


    def __echo(self, update: Update, context: CallbackContext):
        id = update.effective_chat.id
        print(f"teste #{id}")
        Thread(target=self.__itermitant_message_sender, args=(id,), daemon=True).start()
        context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

