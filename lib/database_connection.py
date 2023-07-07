import psycopg
from psycopg.rows import dict_row
import os

class DatabaseConnection:
    DATABASE_NAME = 'shopmanager'

    # Establishes connection to POstgreSQL database
    def connect(self):
        try:
            # Uses psycopgs connect which takes connection string as an argument
            self.connection = psycopg.connect(
                f"postgresql://localhost/{self.DATABASE_NAME}",
                row_factory=dict_row)
            # If connection fails, raises exception
        except psycopg.OperationalError:
            raise Exception(f"Couldn't connect to the database {self.DATABASE_NAME}! " \
                    f"Did you create it using `createdb {self.DATABASE_NAME}`?")
    
    # Seeds database with initial data
    def seed(self, sql_filename):
        self._check_connection()
        if not os.path.exists(sql_filename):
            raise Exception(f"File {sql_filename} does not exist")
        with self.connection.cursor() as cursor:
            cursor.execute(open(sql_filename, "r").read())
            self.connection.commit()
    
    # Enables execution of SQL queries with parameters
    def execute(self, query, params=None):
        self._check_connection()
        with self.connection.cursor() as cursor:
            cursor.execute(query, params)
            if cursor.description is not None:
                result = cursor.fetchall()
            else:
                result = None
            self.connection.commit()
            return result
    
    # Exception message raised when trying to execute a query without an open connection
    CONNECTION_MESSAGE = '' \
        'DatabaseConnection.exec_params: Cannot run a SQL query as ' \
        'the connection to the database was never opened. Did you ' \
        'make sure to call first the method DatabaseConnection.connect` ' \
        'in your app.py file (or in your tests)?'
    
    # This private method checks that we're connected to the database
    def _check_connection(self):
        if self.connection is None:
            raise Exception(self.CONNECTION_MESSAGE)