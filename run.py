import re
from time import sleep

from storage.chatBotStorage import ChatBotStorage
from TelegramBotClient import TelegramBotClient
from TelegramUserClient import TelegramUserClient


def filter_and_foward_message(send_message_func):
    def do_filter_and_foward(message: str):
        print(message)
        for botChat in ChatBotStorage().get_all():
            pattern = re.compile(botChat.filter, re.IGNORECASE)
            if pattern.match(message.replace('\n', ' ')):
                send_message_func(botChat.chat_id, message)
    return do_filter_and_foward


def main():
    botClient = TelegramBotClient()

    userClient = TelegramUserClient(filter_and_foward_message(botClient.send_message))

    botClient.set_join_function(userClient.join_channel)

    botClient.start()
    
    userClient.start()

if __name__ == "__main__":
    main()
