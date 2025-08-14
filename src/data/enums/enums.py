"""
Enums for magic variables in the student room analysis application.
"""

from enum import Enum
from typing import List


class Gender(Enum):
    """Gender enumeration."""
    MALE = 'M'
    FEMALE = 'F'
    
    @classmethod
    def values(cls) -> List[str]:
        return [gender.value for gender in cls]
    
    @classmethod
    def is_valid(cls, value: str) -> bool:
        return value in cls.values()


class Building(Enum):
    """Building enumeration."""
    A = 'A'
    B = 'B'
    C = 'C'
    
    @classmethod
    def values(cls) -> List[str]:
        return [building.value for building in cls]
    
    @classmethod
    def is_valid(cls, value: str) -> bool:
        return value in cls.values()


class DatabaseType(Enum):
    """Database type enumeration."""
    MYSQL = 'mysql'
    POSTGRESQL = 'postgresql'
    SQLITE = 'sqlite'


class QueryType(Enum):
    """Query type enumeration."""
    SELECT = 'SELECT'
    INSERT = 'INSERT'
    UPDATE = 'UPDATE'
    DELETE = 'DELETE'
    CREATE = 'CREATE'
    DROP = 'DROP'


class AnalysisType(Enum):
    """Analysis type enumeration."""
    ROOM_OCCUPANCY = 'room_occupancy'
    AGE_STATISTICS = 'age_statistics'
    GENDER_DISTRIBUTION = 'gender_distribution'
    AGE_DIFFERENCES = 'age_differences'
    BUILDING_STATISTICS = 'building_statistics'


class DataSource(Enum):
    """Data source enumeration."""
    JSON = 'json'
    CSV = 'csv'
    DATABASE = 'database'
    API = 'api'


class SortOrder(Enum):
    """Sort order enumeration."""
    ASC = 'ASC'
    DESC = 'DESC'


class Constants:
    """Application constants."""
    MIN_AGE = 0
    MAX_AGE = 150
    MIN_CAPACITY = 1
    MAX_CAPACITY = 10
    MAX_NAME_LENGTH = 100
    MAX_ROOM_NUMBER_LENGTH = 10
    MAX_BUILDING_LENGTH = 10
    DEFAULT_QUERY_LIMIT = 10
    DEFAULT_STUDENTS_FILE = 'data/students.json'
    DEFAULT_ROOMS_FILE = 'data/rooms.json'
    DEFAULT_DB_HOST = 'localhost'
    DEFAULT_DB_PORT = 3306
    DEFAULT_DB_CHARSET = 'utf8mb4'
    DEFAULT_DB_COLLATION = 'utf8mb4_unicode_ci'
    ERROR_INVALID_GENDER = "Student sex must be 'M' or 'F'"
    ERROR_INVALID_AGE = f"Student age must be between {MIN_AGE} and {MAX_AGE}"
    ERROR_INVALID_CAPACITY = f"Room capacity must be between {MIN_CAPACITY} and {MAX_CAPACITY}"
    ERROR_INVALID_BUILDING = f"Building must be one of: {', '.join(Building.values())}"
    SUCCESS_DB_CONNECTED = "Successfully connected to MySQL database"
    SUCCESS_DB_CLOSED = "Database connection closed"
    SUCCESS_SCHEMA_CREATED = "Database schema created successfully"
    SUCCESS_DATA_INSERTED = "Data inserted successfully"
    STATUS_LOADING_DATA = "Loading data from JSON files..."
    STATUS_CREATING_SCHEMA = "Creating database schema..."
    STATUS_INSERTING_DATA = "Inserting data into database..."
    STATUS_RUNNING_ANALYSIS = "Running analysis queries..."
