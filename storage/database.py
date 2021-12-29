from sqlalchemy import create_engine
from config import DATABASE_URL
from sqlalchemy.orm import sessionmaker
from storage.tables import Base


def get_database_session():
    engine = create_engine(DATABASE_URL, echo=True)
    Base.metadata.create_all(engine)
    session_class = sessionmaker(bind=engine)
    return session_class()


def insert_or_update(table_object, session):
    session.merge(table_object)
    try:
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        return False



