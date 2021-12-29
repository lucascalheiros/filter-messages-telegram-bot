from storage.database import get_database_session, insert_or_update
from storage.tables import ChatMessage


class ChatMessageStorage:
    def __init__(self):
        self.session = get_database_session()

    def get_all(self):
        return self.session.query(ChatMessage).all()

    def insert(self, chat_message: ChatMessage):
        insert_or_update(chat_message, self.session)
