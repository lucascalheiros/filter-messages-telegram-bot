from threading import Thread

from telethon import TelegramClient, events

from config import API_HASH, API_ID


class TelegramUserClient:

    def __init__(self, filter_and_foward_message) -> None:
        self.started = False
        self.filter_and_foward_message = filter_and_foward_message

    def start(self):
        self.__do_start__()

    def __do_start__(self):
        self.client = TelegramClient('auth', API_ID, API_HASH)

        @self.client.on(events.NewMessage)
        async def handler(event):
            self.filter_and_foward_message(event.raw_text)

        self.client.start()
        self.client.run_until_disconnected()



