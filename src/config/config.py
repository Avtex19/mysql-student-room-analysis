"""
Configuration for Student Room Analysis.

This module provides configuration management using dataclasses.
"""

from dataclasses import dataclass
from typing import Dict, Any
from src.data.enums import DatabaseType, Constants


@dataclass
class DatabaseConfig:
    """Database configuration."""
    host: str
    user: str
    password: str
    database: str
    port: int
    charset: str
    collation: str
    db_type: DatabaseType = DatabaseType.MYSQL

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for mysql-connector."""
        return {
            'host': self.host,
            'user': self.user,
            'password': self.password,
            'database': self.database,
            'port': self.port,
            'charset': self.charset,
            'collation': self.collation
        }


@dataclass
class FilePaths:
    """File path configuration."""
    students_file: str
    rooms_file: str


@dataclass
class DatabaseSchema:
    """Database schema configuration."""
    create_database_sql: str
    create_rooms_table_sql: str
    create_students_table_sql: str


@dataclass
class AppConfig:
    """Main application configuration."""
    database: DatabaseConfig
    files: FilePaths
    schema: DatabaseSchema


DEFAULT_DB_CONFIG = DatabaseConfig(
    host=Constants.DEFAULT_DB_HOST,
    user='root',
    password='',
    database='student_room_db',
    port=Constants.DEFAULT_DB_PORT,
    charset=Constants.DEFAULT_DB_CHARSET,
    collation=Constants.DEFAULT_DB_COLLATION,
    db_type=DatabaseType.MYSQL
)

DEFAULT_FILE_PATHS = FilePaths(
    students_file=Constants.DEFAULT_STUDENTS_FILE,
    rooms_file=Constants.DEFAULT_ROOMS_FILE
)

DEFAULT_SCHEMA = DatabaseSchema(
    create_database_sql="CREATE DATABASE IF NOT EXISTS student_room_db",
    create_rooms_table_sql=f"""
    CREATE TABLE IF NOT EXISTS rooms (
        id INT PRIMARY KEY,
        number VARCHAR({Constants.MAX_ROOM_NUMBER_LENGTH}) NOT NULL,
        building VARCHAR({Constants.MAX_BUILDING_LENGTH}) NOT NULL,
        capacity INT NOT NULL,
        INDEX idx_building (building),
        INDEX idx_capacity (capacity)
    )
    """,
    create_students_table_sql=f"""
    CREATE TABLE IF NOT EXISTS students (
        id INT PRIMARY KEY,
        name VARCHAR({Constants.MAX_NAME_LENGTH}) NOT NULL,
        age INT NOT NULL,
        sex CHAR(1) NOT NULL,
        room_id INT NOT NULL,
        FOREIGN KEY (room_id) REFERENCES rooms(id),
        INDEX idx_room_id (room_id),
        INDEX idx_age (age),
        INDEX idx_sex (sex),
        INDEX idx_age_sex (age, sex)
    )
    """
)

APP_CONFIG = AppConfig(
    database=DEFAULT_DB_CONFIG,
    files=DEFAULT_FILE_PATHS,
    schema=DEFAULT_SCHEMA
)

DB_CONFIG = DEFAULT_DB_CONFIG.to_dict()
STUDENTS_FILE = DEFAULT_FILE_PATHS.students_file
ROOMS_FILE = DEFAULT_FILE_PATHS.rooms_file
CREATE_DATABASE_SQL = DEFAULT_SCHEMA.create_database_sql
CREATE_ROOMS_TABLE_SQL = DEFAULT_SCHEMA.create_rooms_table_sql
CREATE_STUDENTS_TABLE_SQL = DEFAULT_SCHEMA.create_students_table_sql
