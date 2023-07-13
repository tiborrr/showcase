# test_db.py
# Standard library imports
import pytest

# Third party imports
from sqlalchemy import text, inspect
from sqlalchemy.orm import Session

@pytest.mark.usefixtures('session')
class TestDatabase:
    REPORTING_TABLES = [
        'user', 'post', 'comment'
    ]

    def test_database_connectivity(self, session: Session):
        result = session.execute(text('SELECT 1'))
        assert result.scalar() == 1

    @pytest.mark.parametrize("expected_table", REPORTING_TABLES)
    def test_tables_created(self, expected_table, session: Session):
        inspector = inspect(session.get_bind())
        actual_tables = set(inspector.get_table_names())
        assert expected_table in actual_tables
