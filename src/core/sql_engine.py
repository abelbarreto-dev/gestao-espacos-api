from os import getenv

from dotenv import load_dotenv
from sqlalchemy import create_engine, Engine

load_dotenv()


database_url = getenv("DATABASE_URL")


def engine() -> Engine:
    return create_engine(database_url)
