# database.py
# Standard library imports
import os

# Third library imports
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from backend.app.config import DB_URL

sqlalchemy_url = os.getenv('SHOWCASE_TEST_DB_URL', DB_URL)

engine = create_engine(DB_URL)

Sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()