import logging
import string
from time import sleep

from TelegramBotClient import TelegramBotClient
from TelegramUserClient import TelegramUserClient
from storage.chatMessageStorage import ChatMessageStorage
from storage.chatBotStorage import ChatBotStorage
import re

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

chatBotStorage = ChatBotStorage()

botClient = TelegramBotClient(chatBotStorage)


def filter_and_foward_message(message: string):
    print(message)
    for botChat in chatBotStorage.get_all():
        pattern = re.compile(botChat.filter, re.IGNORECASE)
        if pattern.match(message.replace('\n', ' ')):
            botClient.send_message(botChat.chat_id, message)


userClient = TelegramUserClient(ChatMessageStorage(), filter_and_foward_message)

botClient.start()
userClient.start()

while True:
    sleep(5)

# print(f"teste #{chat_id}")
# Thread(target=self.__itermitant_message_sender, args=(chat_id,), daemon=True).start()
