"""
Report Generator protocol for formatted output.
"""

from typing import List, Tuple
from abc import ABC, abstractmethod


class ReportGenerator(ABC):
    """Abstract base class for report generators."""

    @abstractmethod
    def format_rooms_with_student_count(self, data: List[Tuple]) -> str:
        """Format rooms with student count data."""
        pass

    @abstractmethod
    def format_top_rooms_by_avg_age(self, data: List[Tuple]) -> str:
        """Format top rooms by average age data."""
        pass

    @abstractmethod
    def format_top_rooms_by_age_difference(self, data: List[Tuple]) -> str:
        """Format top rooms by age difference data."""
        pass

    @abstractmethod
    def format_rooms_with_mixed_sex(self, data: List[Tuple]) -> str:
        """Format rooms with mixed sex data."""
        pass
