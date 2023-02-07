from utils.logger import logger


class BaseSession:
    def __init__(self, db_connector) -> None:
        self.database_connector = db_connector
        self.Session = self.database_connector.Session

    def __enter__(self):
        logger.info("Opening db session...")
        self.session = self.Session()
        return self.session

    def __exit__(self, *exc):
        logger.info("Closing db session...")
        self.session.close()
        logger.info("Closed db session")
