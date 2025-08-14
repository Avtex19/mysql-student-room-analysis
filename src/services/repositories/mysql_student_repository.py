"""
MySQL Student Repository implementation for database operations.
"""

from typing import List, Optional
from src.data.models import Student


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
