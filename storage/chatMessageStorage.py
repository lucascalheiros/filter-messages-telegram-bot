from storage.database import get_database_session
from storage.tables import ChatMessage


class ChatMessageStorage:
    def __init__(self):
        self.session = get_database_session()

    def get_all(self):
        self.session.query(ChatMessage).all()

    def insert(self, chat_bot: ChatMessage):
        self.session.add(chat_bot)
