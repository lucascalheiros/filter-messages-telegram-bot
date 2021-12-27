import asyncio
import logging
from TelegramBotClient import TelegramBotClient
import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# botClient = TelegramBotClient()
# botClient.startbot()


from telethon import TelegramClient, client, events

# Use your own values from my.telegram.org
api_id = config.API_ID
api_hash = config.API_HASH

# The first parameter is the .session file name (absolute paths allowed)
client = TelegramClient('lucas', api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    message = event.raw_text
    print(message)


client.start()
client.run_until_disconnected()