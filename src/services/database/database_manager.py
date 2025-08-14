"""
Database Manager for Student Room Analysis.

This module handles database operations and schema management.
"""

import mysql.connector
from typing import List, Optional
from src.config.config import *
from src.data.models import Room, Student
from src.data.enums import Constants
from ..connections import DatabaseConnection
from ..repositories import MySQLRoomRepository, MySQLStudentRepository


class DatabaseManager:
    """Manages database operations for the student room analysis."""

    def __init__(self, connection: DatabaseConnection):
        self.connection = connection
        self.room_repository = MySQLRoomRepository(connection)
        self.student_repository = MySQLStudentRepository(connection)

    def create_database(self):
        """Create the database if it doesn't exist."""
        try:
            db_config = self.connection.config.copy()
            db_config.pop('database', None)
            temp_connection = mysql.connector.connect(**db_config)
            temp_cursor = temp_connection.cursor()
            temp_cursor.execute(CREATE_DATABASE_SQL)
            temp_cursor.close()
            temp_connection.close()
        except mysql.connector.Error as e:
            print(f"Error creating database: {e}")
            raise

    def create_schema(self):
        """Create database tables."""
        try:
            self.connection.execute(CREATE_ROOMS_TABLE_SQL)
            self.connection.execute(CREATE_STUDENTS_TABLE_SQL)
            print(Constants.SUCCESS_SCHEMA_CREATED)
        except mysql.connector.Error as e:
            print(f"Error creating schema: {e}")
            raise

    def insert_rooms(self, rooms: List[Room]):
        """Insert rooms into the database."""
        try:
            self.room_repository.bulk_create(rooms)
            print(f"Inserted {len(rooms)} rooms")
        except Exception as e:
            print(f"Error inserting rooms: {e}")
            raise

    def insert_students(self, students: List[Student]):
        """Insert students into the database."""
        try:
            self.student_repository.bulk_create(students)
            print(f"Inserted {len(students)} students")
            print(Constants.SUCCESS_DATA_INSERTED)
        except Exception as e:
            print(f"Error inserting students: {e}")
            raise
