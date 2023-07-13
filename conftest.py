# Standard library imports
import os

# Third party imports
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database, database_exists
import alembic.command
import alembic.config

# Local application imports
from backend.app.database.database import Sessionmaker
from backend.app.config import ALEMBIC_INI, TEST_DB_URL

os.environ['SHOWCASE_TEST_DB_URL'] = TEST_DB_URL

engine = create_engine(TEST_DB_URL)
Sessionmaker = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_test_database():
    # Check if the database already exists
    if not database_exists(engine.url):
        # Create the test database
        create_database(engine.url)

def drop_test_database():
    if database_exists(engine.url):
        drop_database(engine.url)

@pytest.fixture(autouse=True, scope='session')
def session():
    # Create the test database
    create_test_database()

    # Run migrations
    config = alembic.config.Config(ALEMBIC_INI)
    alembic.command.upgrade(config, 'head')

    # Provide the session to the tests
    session = Sessionmaker()
    yield session

    # Tear down the session
    session.close()

    # Revert migrations
    alembic.command.downgrade(config, 'base')

    # Drop database
    drop_test_database()
