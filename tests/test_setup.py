#!/usr/bin/env python3
"""
Test setup script for the student room analysis application.

This script verifies that the core components are working correctly
without requiring a MySQL connection.
"""

import os
import sys
import json
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data import StudentDataLoader, RoomDataLoader
from src.services import ConsoleReportGenerator
from src.utils import OptimizationAdvisor


def test_data_loading():
    """Test data loading functionality."""
    print("Testing data loading...")
    
    students_loader = StudentDataLoader()
    students = students_loader.load_models()
    print(f"✓ Successfully loaded {len(students)} students")
    
    rooms_loader = RoomDataLoader()
    rooms = rooms_loader.load_models()
    print(f"✓ Successfully loaded {len(rooms)} rooms")
    
    if students and hasattr(students[0], 'id') and hasattr(students[0], 'room_id'):
        print("✓ Students data structure is correct")
    else:
        print("✗ Students data structure is incorrect")
        return False
    
    if rooms and hasattr(rooms[0], 'id') and hasattr(rooms[0], 'capacity'):
        print("✓ Rooms data structure is correct")
    else:
        print("✗ Rooms data structure is incorrect")
        return False
    
    return True


def test_report_generator():
    """Test report generator functionality."""
    print("\nTesting report generator...")
    
    try:
        generator = ConsoleReportGenerator()
        
        sample_data = [
            (101, "101", "A", 2, 2),
            (102, "102", "A", 2, 1),
            (103, "103", "B", 2, 2)
        ]
        
        report = generator.format_rooms_with_student_count(sample_data)
        if "ROOMS AND STUDENT COUNT" in report:
            print("✓ Report generator is working correctly")
            return True
        else:
            print("✗ Report generator output is incorrect")
            return False
            
    except Exception as e:
        print(f"✗ Error testing report generator: {e}")
        return False


def test_optimization_advisor():
    """Test optimization advisor functionality."""
    print("\nTesting optimization advisor...")
    
    try:
        advisor = OptimizationAdvisor()
        statements = advisor.get_create_index_statements()
        
        if len(statements) > 0 and all("CREATE INDEX" in stmt for stmt in statements):
            print("✓ Optimization advisor is working correctly")
            return True
        else:
            print("✗ Optimization advisor output is incorrect")
            return False
            
    except Exception as e:
        print(f"✗ Error testing optimization advisor: {e}")
        return False


def test_json_files():
    """Test JSON file structure."""
    print("\nTesting JSON files...")
    
    try:
        with open('data/students.json', 'r') as f:
            students = json.load(f)
        
        if isinstance(students, list) and len(students) > 0:
            required_fields = ['id', 'name', 'age', 'sex', 'room_id']
            if all(field in students[0] for field in required_fields):
                print("✓ students.json structure is correct")
            else:
                print("✗ students.json missing required fields")
                return False
        else:
            print("✗ students.json is not a valid list")
            return False
        
        with open('data/rooms.json', 'r') as f:
            rooms = json.load(f)
        
        if isinstance(rooms, list) and len(rooms) > 0:
            required_fields = ['id', 'number', 'building', 'capacity']
            if all(field in rooms[0] for field in required_fields):
                print("✓ rooms.json structure is correct")
            else:
                print("✗ rooms.json missing required fields")
                return False
        else:
            print("✗ rooms.json is not a valid list")
            return False
        
        return True
        
    except FileNotFoundError as e:
        print(f"✗ JSON file not found: {e}")
        return False
    except json.JSONDecodeError as e:
        print(f"✗ Invalid JSON format: {e}")
        return False
    except Exception as e:
        print(f"✗ Error testing JSON files: {e}")
        return False


def main():
    """Run all tests."""
    print("RUNNING TEST SUITE")
    print("=" * 50)
    
    tests = [
        test_data_loading,
        test_report_generator,
        test_optimization_advisor,
        test_json_files
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"✗ Test {test.__name__} failed with exception: {e}")
    
    print("\n" + "=" * 50)
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("All tests passed! The application is ready to run.")
        return True
    else:
        print("Some tests failed. Please check the issues above.")
        return False


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
