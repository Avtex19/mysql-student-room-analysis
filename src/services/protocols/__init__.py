"""
Protocols package for service interfaces.
"""

from .query_service_protocol import QueryService
from .report_generator_protocol import ReportGenerator

__all__ = ['QueryService', 'ReportGenerator']
