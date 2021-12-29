from storage.database import get_database_session
from storage.tables import ChatBot


class ChatBotStorage:
    def __init__(self):
        self.session = get_database_session()

    def get_all(self):
        self.session.query(ChatBot).all()

    def insert(self, chat_bot: ChatBot):
        self.session.add(chat_bot)
