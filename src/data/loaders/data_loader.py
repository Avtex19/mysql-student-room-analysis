"""
Data Loader for Student Room Analysis.

This module handles loading data from various sources.
"""

import json
from typing import List, Dict, Any, Protocol
from abc import ABC, abstractmethod
from ..models import Room, Student
from ..enums import Constants


class DataValidator(Protocol):
    """Protocol for data validation."""
    
    @staticmethod
    def validate_room_data(data: Dict[str, Any]) -> bool:
        """Validate room data."""
        ...
    
    @staticmethod
    def validate_student_data(data: Dict[str, Any]) -> bool:
        """Validate student data."""
        ...


class JsonDataValidator:
    """JSON data validator implementation."""
    
    @staticmethod
    def validate_room_data(data: Dict[str, Any]) -> bool:
        """Validate room data structure."""
        required_fields = ['id', 'number', 'building', 'capacity']
        return all(field in data for field in required_fields)
    
    @staticmethod
    def validate_student_data(data: Dict[str, Any]) -> bool:
        """Validate student data structure."""
        required_fields = ['id', 'name', 'age', 'sex', 'room_id']
        return all(field in data for field in required_fields)


class DataLoader(ABC):
    """Abstract base class for data loaders."""
    
    @abstractmethod
    def load(self) -> List[Dict[str, Any]]:
        """Load data and return as list of dictionaries."""
        pass


class JsonDataLoader(DataLoader):
    """JSON file data loader."""
    
    def __init__(self, file_path: str, validator: DataValidator):
        self.file_path = file_path
        self.validator = validator
    
    def load(self) -> List[Dict[str, Any]]:
        """Load data from JSON file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                data = json.load(file)
            
            if not isinstance(data, list):
                raise ValueError(f"Expected list in {self.file_path}, got {type(data)}")
            
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {self.file_path}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {self.file_path}: {e}")


class ModelDataLoader(ABC):
    """Abstract base class for loading data into models."""
    
    @abstractmethod
    def load_models(self) -> List[Any]:
        """Load data and return as list of model objects."""
        pass


class RoomDataLoader(ModelDataLoader):
    """Loader for Room models."""
    
    def __init__(self, file_path: str = Constants.DEFAULT_ROOMS_FILE):
        self.json_loader = JsonDataLoader(file_path, JsonDataValidator())
    
    def load_models(self) -> List[Room]:
        """Load rooms from JSON and convert to Room objects."""
        raw_data = self.json_loader.load()
        rooms = []
        
        for data in raw_data:
            if JsonDataValidator.validate_room_data(data):
                room = Room(
                    id=data['id'],
                    number=data['number'],
                    building=data['building'],
                    capacity=data['capacity']
                )
                rooms.append(room)
        
        return rooms


class StudentDataLoader(ModelDataLoader):
    """Loader for Student models."""
    
    def __init__(self, file_path: str = Constants.DEFAULT_STUDENTS_FILE):
        self.json_loader = JsonDataLoader(file_path, JsonDataValidator())
    
    def load_models(self) -> List[Student]:
        """Load students from JSON and convert to Student objects."""
        raw_data = self.json_loader.load()
        students = []
        
        for data in raw_data:
            if JsonDataValidator.validate_student_data(data):
                student = Student(
                    id=data['id'],
                    name=data['name'],
                    age=data['age'],
                    sex=data['sex'],
                    room_id=data['room_id']
                )
                students.append(student)
        
        return students
