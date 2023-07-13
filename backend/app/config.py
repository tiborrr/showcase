# config.py
# Standard library imports
import os
import pathlib

config = os.environ

DB_USER = config["SHOWCASE_DB_USER"]
DB_PASS = config["SHOWCASE_DB_PASS"]
DB_NAME = config["SHOWCASE_DB_NAME"]
DB_HOST = config["SHOWCASE_DB_HOST"]
DB_PORT = config["SHOWCASE_DB_PORT"]
DB_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
TEST_DB_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/test_{DB_NAME}"

FRONTEND_HOST = config["SHOWCASE_FRONTEND_HOST"]
FRONTEND_PORT = config["SHOWCASE_FRONTEND_PORT"]
FRONTEND_URL = f"http://{FRONTEND_HOST}:{FRONTEND_PORT}"

PROJECT_DIR = pathlib.Path(__file__).parent.parent.parent
ALEMBIC_DIR = PROJECT_DIR / "alembic"
ALEMBIC_INI = PROJECT_DIR / "alembic.ini"

print(ALEMBIC_INI)