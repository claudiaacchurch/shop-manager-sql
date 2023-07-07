import pytest
from lib.database_connection import DatabaseConnection

# It creates an database connection (object) that we can be used in tests
@pytest.fixture
def db_connection():
    conn = DatabaseConnection()
    conn.connect()
    return conn