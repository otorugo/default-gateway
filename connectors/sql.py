from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from constants import DB_NAME, DRIVER, USER, HOST,PASSWORD


class SQLConnector:
    def __init__(self):
        self.engine = create_engine(f"{DRIVER}://{USER}:{PASSWORD}@{HOST}/{DB_NAME}")
        self.Base = declarative_base()
        self.Session = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine
        )


db_connector = SQLConnector()
