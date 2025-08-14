"""
Query Service protocol for database operations.
"""

from typing import List, Tuple
from abc import ABC, abstractmethod


class QueryService(ABC):
    """Abstract base class for query services."""
    
    @abstractmethod
    def execute_query(self, query: str, params: tuple = None) -> List[Tuple]:
        """Execute a query and return results."""
        pass
