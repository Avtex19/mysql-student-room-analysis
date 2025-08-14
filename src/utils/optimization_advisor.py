"""
Optimization Advisor for Student Room Analysis.

This module provides database optimization recommendations.
"""

from typing import List


class OptimizationAdvisor:
    """Provides database optimization recommendations."""

    def __init__(self):
        self.recommendations = []

    def generate_report(self):
        """Generate optimization recommendations report."""
        print("\nDATABASE OPTIMIZATION RECOMMENDATIONS")
        print("=" * 60)
        
        self._add_existing_indexes()
        self._add_additional_recommendations()
        self._add_query_optimizations()
        self._add_performance_tips()
        
        for i, recommendation in enumerate(self.recommendations, 1):
            print(f"{i}. {recommendation}")
        
        print("\n" + "=" * 60)

    def _add_existing_indexes(self):
        """Add information about existing indexes."""
        self.recommendations.extend([
            "Existing indexes are already created for optimal performance:",
            "  - PRIMARY KEY on rooms.id and students.id",
            "  - INDEX on rooms.building for building-based queries",
            "  - INDEX on rooms.capacity for capacity-based queries",
            "  - INDEX on students.room_id for JOIN operations",
            "  - INDEX on students.age for age-based queries",
            "  - INDEX on students.sex for gender-based queries",
            "  - COMPOSITE INDEX on students.age, students.sex for combined queries"
        ])

    def _add_additional_recommendations(self):
        """Add additional optimization recommendations."""
        self.recommendations.extend([
            "Consider adding these indexes for specific use cases:",
            "  - INDEX on students.name for name-based searches",
            "  - INDEX on rooms.number for room number searches",
            "  - COMPOSITE INDEX on rooms.building, rooms.number for building+room queries"
        ])

    def _add_query_optimizations(self):
        """Add query-specific optimizations."""
        self.recommendations.extend([
            "Query optimization tips:",
            "  - Use LIMIT clauses to restrict result sets",
            "  - Use WHERE clauses before JOINs when possible",
            "  - Consider using EXPLAIN to analyze query execution plans",
            "  - Use appropriate data types (INT vs VARCHAR)",
            "  - Consider partitioning for large datasets"
        ])

    def _add_performance_tips(self):
        """Add general performance tips."""
        self.recommendations.extend([
            "General performance recommendations:",
            "  - Monitor slow query log for performance bottlenecks",
            "  - Regularly update table statistics with ANALYZE TABLE",
            "  - Consider read replicas for heavy read workloads",
            "  - Use connection pooling for multiple concurrent connections",
            "  - Implement caching for frequently accessed data"
        ])

    def get_create_index_statements(self) -> List[str]:
        """Get SQL statements for creating recommended indexes."""
        return [
            "CREATE INDEX idx_student_name ON students(name);",
            "CREATE INDEX idx_room_number ON rooms(number);",
            "CREATE INDEX idx_building_room ON rooms(building, number);",
            "CREATE INDEX idx_student_room_age ON students(room_id, age);",
            "CREATE INDEX idx_student_room_sex ON students(room_id, sex);"
        ]

    def get_optimization_checklist(self) -> List[str]:
        """Get a checklist for database optimization."""
        return [
            "✓ Primary keys defined on all tables",
            "✓ Foreign key constraints properly set",
            "✓ Indexes on frequently queried columns",
            "✓ Composite indexes for multi-column queries",
            "✓ Appropriate data types used",
            "✓ Query execution plans analyzed",
            "✓ Slow query log enabled and monitored",
            "✓ Table statistics updated regularly"
        ]
