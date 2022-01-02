import asyncio
from threading import Thread

from telethon import TelegramClient, events
from telethon.tl.functions.channels import JoinChannelRequest

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

    def join_channel(self, channel_name: str):
        async def do_join_channel():
            try:
                print(f'teste1 {channel_name}')
                channel = await self.client.get_entity(f'https://t.me/joinchat/{channel_name}') 
                print(f'teste2 {channel}')
                await self.client(JoinChannelRequest(channel))
                print('teste3')
            except:
                print('error')
        print('teste0')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(do_join_channel())
