"""
MySQL Connection implementation for Student Room Analysis.
"""

import mysql.connector
from typing import List
from .database_connection import DatabaseConnection
from src.data.enums import Constants


class MySQLConnection(DatabaseConnection):
    """MySQL database connection implementation."""

    def __init__(self, config: dict):
        self.config = config
        self.connection = None
        self.cursor = None

    def connect(self):
        """Establish MySQL connection."""
        try:
            self.connection = mysql.connector.connect(**self.config)
            self.cursor = self.connection.cursor()
            print(Constants.SUCCESS_DB_CONNECTED)
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    def disconnect(self):
        """Close MySQL connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print(Constants.SUCCESS_DB_CLOSED)

    def execute(self, query: str, params: tuple = None):
        """Execute a SQL query."""
        try:
            self.cursor.execute(query, params)
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")
            raise

    def execute_many(self, query: str, params_list: List[tuple]):
        """Execute a SQL query with multiple parameter sets."""
        try:
            self.cursor.executemany(query, params_list)
            self.connection.commit()
        except mysql.connector.Error as e:
            print(f"Error executing batch query: {e}")
            raise

    def fetch_all(self, query: str, params: tuple = None) -> List[tuple]:
        """Fetch all results from a query."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
            raise
