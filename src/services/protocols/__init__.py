"""
Protocols package for service interfaces.
"""

from .room_repository_protocol import RoomRepository
from .student_repository_protocol import StudentRepository
from .query_service_protocol import QueryService
from .report_generator_protocol import ReportGenerator

__all__ = ['RoomRepository', 'StudentRepository', 'QueryService', 'ReportGenerator']
