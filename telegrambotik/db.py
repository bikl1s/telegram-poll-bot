from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, Boolean, PickleType


class DB:
    def __init__(self, DATABASE_FILE):
        self.engine = create_engine(f'sqlite:///{DATABASE_FILE}')
        Session = sessionmaker(bind=self.engine)
        self.Base = declarative_base()
        self.s = Session()
        logger.succes(f"База данных активирована по адресу → {DATABASE_FILE}")