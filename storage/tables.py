from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class ChatBot(Base):
    __tablename__ = 'chat_bot'

    chat_id = Column(Integer, primary_key=True)
    is_active = Column(Boolean)

    def __repr__(self):
        return f'ChatBot {self.chat_id} active: {self.is_active}'
