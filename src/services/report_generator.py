"""
Report Generator for Student Room Analysis.

This module provides formatted output for analysis results.
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


class ConsoleReportGenerator(ReportGenerator):
    """Console-based report generator."""

    def _calculate_column_widths(self, data: List[Tuple], headers: List[str]) -> List[int]:
        """Calculate optimal column widths for formatting."""
        widths = [len(header) for header in headers]
        
        for row in data:
            for i, value in enumerate(row):
                widths[i] = max(widths[i], len(str(value)))
        
        for i in range(len(widths)):
            widths[i] = max(widths[i], 10)
        
        return widths

    def _format_table(self, data: List[Tuple], headers: List[str], title: str) -> str:
        """Format data as a table."""
        if not data:
            return f"\n{title}\nNo data available."
        
        widths = self._calculate_column_widths(data, headers)
        
        header_row = " | ".join(f"{header:<{width}}" for header, width in zip(headers, widths))
        separator = "-" * len(header_row)
        
        rows = []
        for row in data:
            formatted_row = " | ".join(f"{str(value):<{width}}" for value, width in zip(row, widths))
            rows.append(formatted_row)
        
        return f"\n{title}\n{separator}\n{header_row}\n{separator}\n" + "\n".join(rows)

    def format_rooms_with_student_count(self, data: List[Tuple]) -> str:
        """Format rooms with student count data."""
        headers = ["Room ID", "Number", "Building", "Capacity", "Students"]
        return self._format_table(data, headers, "ROOMS AND STUDENT COUNT")

    def format_top_rooms_by_avg_age(self, data: List[Tuple]) -> str:
        """Format top rooms by average age data."""
        headers = ["Room ID", "Number", "Building", "Students", "Avg Age"]
        return self._format_table(data, headers, "TOP 5 ROOMS BY SMALLEST AVERAGE AGE")

    def format_top_rooms_by_age_difference(self, data: List[Tuple]) -> str:
        """Format top rooms by age difference data."""
        headers = ["Room ID", "Number", "Building", "Students", "Age Diff"]
        return self._format_table(data, headers, "TOP 5 ROOMS BY LARGEST AGE DIFFERENCE")

    def format_rooms_with_mixed_sex(self, data: List[Tuple]) -> str:
        """Format rooms with mixed sex data."""
        headers = ["Room ID", "Number", "Building", "Male", "Female", "Total"]
        return self._format_table(data, headers, "ROOMS WITH MIXED SEXES")

    def format_room_occupancy_analysis(self, data: List[Tuple]) -> str:
        """Format room occupancy analysis data."""
        headers = ["Room ID", "Number", "Building", "Capacity", "Occupied", "Percentage"]
        return self._format_table(data, headers, "ROOM OCCUPANCY ANALYSIS")

    def format_age_distribution_by_building(self, data: List[Tuple]) -> str:
        """Format age distribution by building data."""
        headers = ["Building", "Students", "Avg Age", "Min Age", "Max Age"]
        return self._format_table(data, headers, "AGE DISTRIBUTION BY BUILDING")

    def display_rooms_with_student_count(self, data: List[Tuple]):
        """Display rooms with student count."""
        print(self.format_rooms_with_student_count(data))

    def display_top_rooms_by_avg_age(self, data: List[Tuple]):
        """Display top rooms by average age."""
        print(self.format_top_rooms_by_avg_age(data))

    def display_top_rooms_by_age_difference(self, data: List[Tuple]):
        """Display top rooms by age difference."""
        print(self.format_top_rooms_by_age_difference(data))

    def display_rooms_with_mixed_sex(self, data: List[Tuple]):
        """Display rooms with mixed sex."""
        print(self.format_rooms_with_mixed_sex(data))

    def display_room_occupancy_analysis(self, data: List[Tuple]):
        """Display room occupancy analysis."""
        print(self.format_room_occupancy_analysis(data))

    def display_age_distribution_by_building(self, data: List[Tuple]):
        """Display age distribution by building."""
        print(self.format_age_distribution_by_building(data))
