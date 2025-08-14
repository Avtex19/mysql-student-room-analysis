"""
Data models for the student room analysis application.
"""

from dataclasses import dataclass
from typing import Optional
from .enums import Gender, Building, Constants


@dataclass
class Room:
    """Data model for a room."""
    id: int
    number: str
    building: str
    capacity: int
    
    def __post_init__(self):
        """Validate room data after initialization."""
        if self.id <= 0:
            raise ValueError("Room ID must be positive")
        if not self.number:
            raise ValueError("Room number cannot be empty")
        if len(self.number) > Constants.MAX_ROOM_NUMBER_LENGTH:
            raise ValueError(f"Room number cannot exceed {Constants.MAX_ROOM_NUMBER_LENGTH} characters")
        if not Building.is_valid(self.building):
            raise ValueError(Constants.ERROR_INVALID_BUILDING)
        if len(self.building) > Constants.MAX_BUILDING_LENGTH:
            raise ValueError(f"Building name cannot exceed {Constants.MAX_BUILDING_LENGTH} characters")
        if self.capacity < Constants.MIN_CAPACITY or self.capacity > Constants.MAX_CAPACITY:
            raise ValueError(Constants.ERROR_INVALID_CAPACITY)


@dataclass
class Student:
    """Data model for a student."""
    id: int
    name: str
    age: int
    sex: str
    room_id: int
    
    def __post_init__(self):
        """Validate student data after initialization."""
        if self.id <= 0:
            raise ValueError("Student ID must be positive")
        if not self.name:
            raise ValueError("Student name cannot be empty")
        if len(self.name) > Constants.MAX_NAME_LENGTH:
            raise ValueError(f"Student name cannot exceed {Constants.MAX_NAME_LENGTH} characters")
        if self.age < Constants.MIN_AGE or self.age > Constants.MAX_AGE:
            raise ValueError(Constants.ERROR_INVALID_AGE)
        if not Gender.is_valid(self.sex):
            raise ValueError(Constants.ERROR_INVALID_GENDER)
        if self.room_id <= 0:
            raise ValueError("Room ID must be positive")


@dataclass
class RoomOccupancy:
    """Data model for room occupancy statistics."""
    room_id: int
    room_number: str
    building: str
    capacity: int
    current_occupancy: int
    available_spots: int
    occupancy_percentage: float


@dataclass
class AgeStatistics:
    """Data model for age-related statistics."""
    room_id: int
    room_number: str
    building: str
    student_count: int
    average_age: float
    min_age: Optional[int] = None
    max_age: Optional[int] = None
    age_difference: Optional[int] = None


@dataclass
class GenderDistribution:
    """Data model for gender distribution in rooms."""
    room_id: int
    room_number: str
    building: str
    total_students: int
    male_count: int
    female_count: int
    has_mixed_gender: bool
