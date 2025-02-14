from os import getenv

from dotenv import load_dotenv
from sqlalchemy import Engine, create_engine

load_dotenv()


database_url = getenv("DATABASE_URL")


def sync_engine() -> Engine:
    return create_engine(database_url)
