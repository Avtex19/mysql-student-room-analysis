#!/usr/bin/env python3
"""
Student Room Analysis Application Entry Point

This is the main entry point for the application.
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.application.student_room_analyzer import StudentRoomAnalyzer


def main():
    """Main entry point for the application."""
    analyzer = StudentRoomAnalyzer()
    analyzer.run()


if __name__ == "__main__":
    main()
