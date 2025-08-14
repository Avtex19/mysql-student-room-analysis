"""
Student Room Analyzer Application Service.

This module contains the main business logic for the student room analysis application.
"""

from src.config import APP_CONFIG
from src.data import StudentDataLoader, RoomDataLoader
from src.services.connections import MySQLConnection
from src.services.database import DatabaseManager
from src.services.queries import StudentRoomQueryService
from src.services.reports import ConsoleReportGenerator
from src.utils.optimization import OptimizationAdvisor


class StudentRoomAnalyzer:
    """Main application service for student room analysis."""

    def __init__(self, config=None):
        self.connection = None
        self.db_manager = None
        self.query_service = None
        self.report_generator = None
        self.config = config or APP_CONFIG

    def setup_database_connection(self):
        """Setup database connection and services."""
        db_config = self.config.database.to_dict()
        db_config_no_db = db_config.copy()
        db_config_no_db.pop('database', None)
        self.connection = MySQLConnection(db_config_no_db)
        self.connection.connect()
        self.db_manager = DatabaseManager(self.connection)
        self.query_service = StudentRoomQueryService(self.connection)
        self.report_generator = ConsoleReportGenerator()
        print("✓ Database connection and services initialized successfully")

    def create_database_schema(self):
        """Create database and tables."""
        print("Creating database schema...")
        self.db_manager.create_database()
        
        db_config = self.config.database.to_dict()
        self.connection.disconnect()
        self.connection = MySQLConnection(db_config)
        self.connection.connect()
        self.db_manager = DatabaseManager(self.connection)
        self.query_service = StudentRoomQueryService(self.connection)
        
        self.db_manager.create_schema()
        print("✓ Database schema created successfully")

    def load_and_insert_data(self):
        """Load data from JSON files and insert into database."""
        print("Loading and inserting data...")
        students_loader = StudentDataLoader(self.config.files.students_file)
        rooms_loader = RoomDataLoader(self.config.files.rooms_file)
        students = students_loader.load_models()
        rooms = rooms_loader.load_models()
        print(f"✓ Loaded {len(students)} students and {len(rooms)} rooms")
        self.db_manager.insert_rooms(rooms)
        self.db_manager.insert_students(students)
        print("✓ Data inserted successfully")

    def run_analysis(self):
        """Run all analysis queries."""
        print("\nRunning analysis queries...")
        
        self.report_generator.display_rooms_with_student_count(
            self.query_service.get_rooms_with_student_count()
        )
        
        self.report_generator.display_top_rooms_by_avg_age(
            self.query_service.get_top_rooms_by_avg_age()
        )
        
        self.report_generator.display_top_rooms_by_age_difference(
            self.query_service.get_top_rooms_by_age_difference()
        )
        
        self.report_generator.display_rooms_with_mixed_sex(
            self.query_service.get_rooms_with_mixed_sex()
        )
        
        self.report_generator.display_room_occupancy_analysis(
            self.query_service.get_room_occupancy_analysis()
        )
        
        self.report_generator.display_age_distribution_by_building(
            self.query_service.get_age_distribution_by_building()
        )

    def generate_optimization_report(self):
        """Generate optimization recommendations."""
        print("\nGenerating optimization recommendations...")
        advisor = OptimizationAdvisor()
        advisor.generate_report()

    def cleanup(self):
        """Cleanup database connection."""
        if self.connection:
            self.connection.disconnect()

    def run(self):
        """Run the complete analysis workflow."""
        print("Starting Student Room Analysis Application")
        print("="*60)
        print(f"Using configuration: {self.config.database.database} on {self.config.database.host}:{self.config.database.port}")
        print("="*60)
        
        try:
            self.setup_database_connection()
            self.create_database_schema()
            self.load_and_insert_data()
            self.run_analysis()
            self.generate_optimization_report()
            
            print("\n" + "="*60)
            print("Analysis completed successfully!")
            print("="*60)
            
        except Exception as e:
            print(f"Error during analysis: {e}")
            raise
        finally:
            self.cleanup()

