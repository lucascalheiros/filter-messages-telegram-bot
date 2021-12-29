from threading import Thread

from telethon import TelegramClient, events

from config import API_ID, API_HASH
from storage.chatMessageStorage import ChatMessageStorage
from storage.tables import ChatMessage


class TelegramUserClient:

    def __init__(self, chat_message_storage: ChatMessageStorage, filter_and_foward_message) -> None:
        self.started = False
        self.chat_message_storage = chat_message_storage
        self.filter_and_foward_message = filter_and_foward_message

    def start(self):
        self.__do_start()
        # if not self.started:
        #     Thread(target=self.__do_start, args=(), daemon=True).start()

    def __do_start(self):
        self.client = TelegramClient('lucas', API_ID, API_HASH)

        @self.client.on(events.NewMessage)
        async def handler(event):
            self.filter_and_foward_message(event.raw_text)
            # message =
            # self.chat_message_storage.insert(ChatMessage(content=message))
            # print(message)
            # print(self.chat_message_storage.get_all())

        self.client.start()
        self.client.run_until_disconnected()



