"""
Database Manager for Student Room Analysis.

This module handles database connections, schema creation, and data operations.
"""

import mysql.connector
from typing import List, Optional
from abc import ABC, abstractmethod
from src.config.config import *
from src.data.models import Room, Student
from src.data.enums import Constants
from .repository import MySQLRoomRepository, MySQLStudentRepository


class DatabaseConnection(ABC):
    """Abstract base class for database connections."""

    @abstractmethod
    def connect(self):
        """Establish database connection."""
        pass

    @abstractmethod
    def disconnect(self):
        """Close database connection."""
        pass

    @abstractmethod
    def execute(self, query: str, params: tuple = None):
        """Execute a SQL query."""
        pass

    @abstractmethod
    def fetch_all(self, query: str, params: tuple = None) -> List[tuple]:
        """Fetch all results from a query."""
        pass

    @abstractmethod
    def fetch_one(self, query: str, params: tuple = None) -> Optional[tuple]:
        """Fetch one result from a query."""
        pass


class MySQLConnection(DatabaseConnection):
    """MySQL database connection implementation."""

    def __init__(self, config: Dict[str, Any]):
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

    def fetch_all(self, query: str, params: tuple = None) -> List[tuple]:
        """Fetch all results from a query."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchall()
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
            raise

    def fetch_one(self, query: str, params: tuple = None) -> Optional[tuple]:
        """Fetch one result from a query."""
        try:
            self.cursor.execute(query, params)
            return self.cursor.fetchone()
        except mysql.connector.Error as e:
            print(f"Error fetching data: {e}")
            raise


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

    def get_all_rooms(self) -> List[Room]:
        """Get all rooms from the database."""
        return self.room_repository.get_all()

    def get_all_students(self) -> List[Student]:
        """Get all students from the database."""
        return self.student_repository.get_all()

    def get_students_by_room(self, room_id: int) -> List[Student]:
        """Get students by room ID."""
        return self.student_repository.get_by_room_id(room_id)

    def get_room_by_id(self, room_id: int) -> Optional[Room]:
        """Get room by ID."""
        return self.room_repository.get_by_id(room_id)

    def get_student_by_id(self, student_id: int) -> Optional[Student]:
        """Get student by ID."""
        return self.student_repository.get_by_id(student_id)
