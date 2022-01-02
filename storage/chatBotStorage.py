from storage.database import get_database_session, insert_or_update
from storage.tables import ChatBot


class ChatBotStorage:
    def __init__(self):
        self.session = get_database_session()

    def get_all(self) -> list[ChatBot]:
        return self.session.query(ChatBot).all()

    def get_by_chat_id(self, chat_id: int) -> ChatBot:
        return self.session.query(ChatBot).get(chat_id)

    def insert(self, chat_bot: ChatBot):
        insert_or_update(chat_bot, self.session)
