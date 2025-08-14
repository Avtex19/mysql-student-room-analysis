"""
MySQL Room Repository implementation for database operations.
"""

from typing import List, Optional
from src.data.models import Room


class MySQLRoomRepository:
    """MySQL implementation of room repository."""
    
    def __init__(self, connection):
        self.connection = connection
    
    def create(self, room: Room) -> None:
        """Create a room."""
        query = """
        INSERT INTO rooms (id, number, building, capacity) 
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
        number = VALUES(number), 
        building = VALUES(building), 
        capacity = VALUES(capacity)
        """
        self.connection.execute(query, (room.id, room.number, room.building, room.capacity))
    
    def get_all(self) -> List[Room]:
        """Get all rooms."""
        query = "SELECT id, number, building, capacity FROM rooms ORDER BY id"
        results = self.connection.fetch_all(query)
        return [
            Room(id=row[0], number=row[1], building=row[2], capacity=row[3])
            for row in results
        ]
    
    def bulk_create(self, rooms: List[Room]) -> None:
        """Create multiple rooms."""
        query = """
        INSERT INTO rooms (id, number, building, capacity) 
        VALUES (%s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
        number = VALUES(number), 
        building = VALUES(building), 
        capacity = VALUES(capacity)
        """
        params_list = [
            (room.id, room.number, room.building, room.capacity)
            for room in rooms
        ]
        self.connection.execute_many(query, params_list)
