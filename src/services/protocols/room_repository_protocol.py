"""
Room Repository protocol for database operations.
"""

from typing import List, Optional, Protocol
from src.data.models import Room


class RoomRepository(Protocol):
    """Protocol for room repository operations."""
    
    def create(self, room: Room) -> None:
        """Create a room."""
        ...
    
    def get_by_id(self, room_id: int) -> Optional[Room]:
        """Get room by ID."""
        ...
    
    def get_all(self) -> List[Room]:
        """Get all rooms."""
        ...
    
    def update(self, room: Room) -> None:
        """Update a room."""
        ...
    
    def delete(self, room_id: int) -> None:
        """Delete a room."""
        ...
    
    def bulk_create(self, rooms: List[Room]) -> None:
        """Create multiple rooms."""
        ...
