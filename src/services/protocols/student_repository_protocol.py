"""
Student Repository protocol for database operations.
"""

from typing import List, Optional, Protocol
from src.data.models import Student


class StudentRepository(Protocol):
    """Protocol for student repository operations."""
    
    def create(self, student: Student) -> None:
        """Create a student."""
        ...
    
    def get_by_id(self, student_id: int) -> Optional[Student]:
        """Get student by ID."""
        ...
    
    def get_all(self) -> List[Student]:
        """Get all students."""
        ...
    
    def get_by_room_id(self, room_id: int) -> List[Student]:
        """Get students by room ID."""
        ...
    
    def update(self, student: Student) -> None:
        """Update a student."""
        ...
    
    def delete(self, student_id: int) -> None:
        """Delete a student."""
        ...
    
    def bulk_create(self, students: List[Student]) -> None:
        """Create multiple students."""
        ...
