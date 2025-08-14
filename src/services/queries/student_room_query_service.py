"""
Student Room Query Service for database analysis queries.
"""

from typing import List, Tuple
from ..protocols.query_service_protocol import QueryService
from ..connections.database_connection import DatabaseConnection
from src.data.enums import QueryType, SortOrder, Constants, Gender


class StudentRoomQueryService(QueryService):
    """Concrete implementation for student-room analysis queries."""

    def __init__(self, connection: DatabaseConnection):
        self.connection = connection

    def execute_query(self, query: str, params: tuple = None) -> List[Tuple]:
        """Execute a SQL query and return results."""
        return self.connection.fetch_all(query, params)

    def get_rooms_with_student_count(self) -> List[Tuple]:
        """Get list of rooms and the number of students in each."""
        query = f"""
        {QueryType.SELECT.value}
            r.id,
            r.number,
            r.building,
            r.capacity,
            COUNT(s.id) as student_count
        FROM rooms r
        LEFT JOIN students s ON r.id = s.room_id
        GROUP BY r.id, r.number, r.building, r.capacity
        ORDER BY r.building, r.number
        """
        return self.execute_query(query)

    def get_top_rooms_by_avg_age(self, limit: int = Constants.DEFAULT_QUERY_LIMIT) -> List[Tuple]:
        """Get top rooms with smallest average student age."""
        query = f"""
        {QueryType.SELECT.value}
            r.id,
            r.number,
            r.building,
            COUNT(s.id) as student_count,
            AVG(s.age) as avg_age
        FROM rooms r
        LEFT JOIN students s ON r.id = s.room_id
        GROUP BY r.id, r.number, r.building
        HAVING COUNT(s.id) > 0
        ORDER BY avg_age {SortOrder.ASC.value}
        LIMIT {limit}
        """
        return self.execute_query(query)

    def get_top_rooms_by_age_difference(self, limit: int = Constants.DEFAULT_QUERY_LIMIT) -> List[Tuple]:
        """Get top rooms with largest age difference among students."""
        query = f"""
        {QueryType.SELECT.value}
            r.id,
            r.number,
            r.building,
            COUNT(s.id) as student_count,
            MAX(s.age) - MIN(s.age) as age_difference,
            MIN(s.age) as min_age,
            MAX(s.age) as max_age
        FROM rooms r
        LEFT JOIN students s ON r.id = s.room_id
        GROUP BY r.id, r.number, r.building
        HAVING COUNT(s.id) > 1
        ORDER BY age_difference {SortOrder.DESC.value}
        LIMIT {limit}
        """
        return self.execute_query(query)

    def get_rooms_with_mixed_sex(self) -> List[Tuple]:
        """Get list of rooms where students of different sexes live together."""
        query = f"""
        {QueryType.SELECT.value}
            r.id,
            r.number,
            r.building,
            COUNT(CASE WHEN s.sex = '{Gender.MALE.value}' THEN 1 END) as male_count,
            COUNT(CASE WHEN s.sex = '{Gender.FEMALE.value}' THEN 1 END) as female_count,
            COUNT(s.id) as total_students
        FROM rooms r
        LEFT JOIN students s ON r.id = s.room_id
        GROUP BY r.id, r.number, r.building
        HAVING 
            COUNT(CASE WHEN s.sex = '{Gender.MALE.value}' THEN 1 END) > 0
            AND COUNT(CASE WHEN s.sex = '{Gender.FEMALE.value}' THEN 1 END) > 0
        ORDER BY r.building, r.number
        """
        return self.execute_query(query)

    def get_room_occupancy_analysis(self) -> List[Tuple]:
        """Get room occupancy analysis with capacity and availability."""
        query = f"""
        {QueryType.SELECT.value}
            r.id,
            r.number,
            r.building,
            r.capacity,
            COUNT(s.id) as occupied_spots,
            r.capacity - COUNT(s.id) as available_spots,
            ROUND((COUNT(s.id) / r.capacity) * 100, 2) as occupancy_percentage
        FROM rooms r
        LEFT JOIN students s ON r.id = s.room_id
        GROUP BY r.id, r.number, r.building, r.capacity
        ORDER BY occupancy_percentage {SortOrder.DESC.value}, r.building, r.number
        """
        return self.execute_query(query)

    def get_age_distribution_by_building(self) -> List[Tuple]:
        """Get age distribution statistics by building."""
        query = f"""
        {QueryType.SELECT.value}
            r.building,
            COUNT(s.id) as student_count,
            ROUND(AVG(s.age), 2) as avg_age,
            MIN(s.age) as min_age,
            MAX(s.age) as max_age,
            ROUND(STDDEV(s.age), 2) as std_dev
        FROM rooms r
        LEFT JOIN students s ON r.id = s.room_id
        GROUP BY r.building
        HAVING COUNT(s.id) > 0
        ORDER BY r.building
        """
        return self.execute_query(query)
