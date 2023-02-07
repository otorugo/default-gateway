from os import getenv

from dotenv import load_dotenv

load_dotenv()

DRIVER = getenv("DRIVER")
DB_NAME = getenv("DB_NAME")
USER = getenv("DB_USER")
PASSWORD = getenv("PASSWORD")
HOST = getenv("HOST")
LOG_LEVEL = getenv("LOG_LEVEL")
SECRET_KEY = getenv("SECRET_KEY")
ALG = getenv("ALG")
EXPIRATION_TIME = int(getenv("EXPIRATION_TIME") or 5)
