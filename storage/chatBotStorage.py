from storage.database import get_database_session, insert_or_update
from storage.tables import ChatBot


class ChatBotStorage:
    def __init__(self):
        self.session = get_database_session()

    def get_all(self):
        return self.session.query(ChatBot).all()

    def insert(self, chat_bot: ChatBot):
        insert_or_update(chat_bot, self.session)
