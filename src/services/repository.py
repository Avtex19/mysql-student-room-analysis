"""
Repository pattern for database operations.
"""

from typing import List, Optional, Protocol
from src.data.models import Room, Student


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
    
    def get_by_id(self, room_id: int) -> Optional[Room]:
        """Get room by ID."""
        query = "SELECT id, number, building, capacity FROM rooms WHERE id = %s"
        result = self.connection.fetch_all(query, (room_id,))
        if result:
            row = result[0]
            return Room(id=row[0], number=row[1], building=row[2], capacity=row[3])
        return None
    
    def get_all(self) -> List[Room]:
        """Get all rooms."""
        query = "SELECT id, number, building, capacity FROM rooms ORDER BY id"
        results = self.connection.fetch_all(query)
        return [
            Room(id=row[0], number=row[1], building=row[2], capacity=row[3])
            for row in results
        ]
    
    def update(self, room: Room) -> None:
        """Update a room."""
        query = """
        UPDATE rooms 
        SET number = %s, building = %s, capacity = %s 
        WHERE id = %s
        """
        self.connection.execute(query, (room.number, room.building, room.capacity, room.id))
    
    def delete(self, room_id: int) -> None:
        """Delete a room."""
        query = "DELETE FROM rooms WHERE id = %s"
        self.connection.execute(query, (room_id,))
    
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


class MySQLStudentRepository:
    """MySQL implementation of student repository."""
    
    def __init__(self, connection):
        self.connection = connection
    
    def create(self, student: Student) -> None:
        """Create a student."""
        query = """
        INSERT INTO students (id, name, age, sex, room_id) 
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
        name = VALUES(name), 
        age = VALUES(age), 
        sex = VALUES(sex), 
        room_id = VALUES(room_id)
        """
        self.connection.execute(query, (student.id, student.name, student.age, student.sex, student.room_id))
    
    def get_by_id(self, student_id: int) -> Optional[Student]:
        """Get student by ID."""
        query = "SELECT id, name, age, sex, room_id FROM students WHERE id = %s"
        result = self.connection.fetch_all(query, (student_id,))
        if result:
            row = result[0]
            return Student(id=row[0], name=row[1], age=row[2], sex=row[3], room_id=row[4])
        return None
    
    def get_all(self) -> List[Student]:
        """Get all students."""
        query = "SELECT id, name, age, sex, room_id FROM students ORDER BY id"
        results = self.connection.fetch_all(query)
        return [
            Student(id=row[0], name=row[1], age=row[2], sex=row[3], room_id=row[4])
            for row in results
        ]
    
    def get_by_room_id(self, room_id: int) -> List[Student]:
        """Get students by room ID."""
        query = "SELECT id, name, age, sex, room_id FROM students WHERE room_id = %s ORDER BY id"
        results = self.connection.fetch_all(query, (room_id,))
        return [
            Student(id=row[0], name=row[1], age=row[2], sex=row[3], room_id=row[4])
            for row in results
        ]
    
    def update(self, student: Student) -> None:
        """Update a student."""
        query = """
        UPDATE students 
        SET name = %s, age = %s, sex = %s, room_id = %s 
        WHERE id = %s
        """
        self.connection.execute(query, (student.name, student.age, student.sex, student.room_id, student.id))
    
    def delete(self, student_id: int) -> None:
        """Delete a student."""
        query = "DELETE FROM students WHERE id = %s"
        self.connection.execute(query, (student_id,))
    
    def bulk_create(self, students: List[Student]) -> None:
        """Create multiple students."""
        query = """
        INSERT INTO students (id, name, age, sex, room_id) 
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
        name = VALUES(name), 
        age = VALUES(age), 
        sex = VALUES(sex), 
        room_id = VALUES(room_id)
        """
        params_list = [
            (student.id, student.name, student.age, student.sex, student.room_id)
            for student in students
        ]
        self.connection.execute_many(query, params_list)

