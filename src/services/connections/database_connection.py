"""
Database Connection protocol for Student Room Analysis.
"""

from typing import List, Optional
from abc import ABC, abstractmethod


class DatabaseConnection(ABC):
    """Abstract base class for database connections."""

    @abstractmethod
    def connect(self):
        """Establish database connection."""
        pass

    @abstractmethod
    def disconnect(self):
        """Close database connection."""
        pass

    @abstractmethod
    def execute(self, query: str, params: tuple = None):
        """Execute a SQL query."""
        pass

    @abstractmethod
    def fetch_all(self, query: str, params: tuple = None) -> List[tuple]:
        """Fetch all results from a query."""
        pass

    @abstractmethod
    def fetch_one(self, query: str, params: tuple = None) -> Optional[tuple]:
        """Fetch one result from a query."""
        pass
