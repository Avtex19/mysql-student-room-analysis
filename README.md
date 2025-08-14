# Student Room Analysis - MySQL & Python

A comprehensive Python application for analyzing student room data using MySQL, following SOLID principles.

## Project Overview

This application demonstrates:
- **SOLID Principles** implementation
- **Raw SQL** queries (no ORM)
- **Database-level calculations** for optimal performance
- **Modular architecture** with clear separation of concerns
- **Query optimization** with proper indexing strategies
- **Clean code structure** with one class per file

## Requirements

- Python 3.11+
- MySQL Server 8.0+
- `uv` package manager

## Quick Start

### 1. Setup Environment

```bash
# Clone the repository
git clone <repository-url>
cd mysql-student-room-analysis-1

# Install dependencies using uv
uv sync
```

### 2. Configure Database

Edit `src/config/config.py` and update the database configuration:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'your_mysql_password',  # Set your MySQL password
    'database': 'student_room_db',
    'port': 3306,
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}
```

### 3. Run the Application

```bash
# Run the main analysis
uv run python main.py

# Preview the database structure (no MySQL required)
uv run python src/utils/preview/database_preview.py
```

## Analysis Features

The application performs the following analyses:

### 1. Room Occupancy Analysis
- List of rooms and the number of students in each
- Room capacity vs. current occupancy
- Occupancy percentage calculations

### 2. Age-Based Analysis
- Top 5 rooms with smallest average student age
- Top 5 rooms with largest age difference among students
- Age distribution statistics by building

### 3. Demographic Analysis
- Rooms with students of different sexes
- Gender distribution per room
- Building-wise demographic breakdown

## Architecture

The application follows SOLID principles with a clean, modular structure:

```
├── main.py                  # Main application entry point
├── src/                     # Source code package
│   ├── config/             # Configuration settings
│   │   ├── __init__.py
│   │   └── config.py
│   ├── data/               # Data models and loading
│   │   ├── __init__.py
│   │   ├── data_loader.py
│   │   ├── models.py
│   │   └── enums.py
│   ├── services/           # Core services (one class per file)
│   │   ├── connections/    # Database connections
│   │   │   ├── __init__.py
│   │   │   ├── database_connection.py
│   │   │   └── mysql_connection.py
│   │   ├── protocols/      # Service interfaces
│   │   │   ├── __init__.py
│   │   │   ├── room_repository_protocol.py
│   │   │   ├── student_repository_protocol.py
│   │   │   ├── query_service_protocol.py
│   │   │   └── report_generator_protocol.py
│   │   ├── repositories/   # Repository implementations
│   │   │   ├── __init__.py
│   │   │   ├── mysql_room_repository.py
│   │   │   └── mysql_student_repository.py
│   │   ├── queries/        # Query services
│   │   │   ├── __init__.py
│   │   │   └── student_room_query_service.py
│   │   ├── reports/        # Report generators
│   │   │   ├── __init__.py
│   │   │   └── console_report_generator.py
│   │   └── database/       # Database management
│   │       ├── __init__.py
│   │       └── database_manager.py
│   ├── utils/              # Utility modules (one class per file)
│   │   ├── optimization/   # Optimization utilities
│   │   │   ├── __init__.py
│   │   │   └── optimization_advisor.py
│   │   └── preview/        # Preview utilities
│   │       ├── __init__.py
│   │       └── database_preview.py
│   └── application/        # Business logic
│       ├── __init__.py
│       └── student_room_analyzer.py
├── data/                   # Data files
│   ├── students.json
│   └── rooms.json
├── reports/                # Analysis reports by subtask
│   ├── 00_summary_report.txt
│   ├── 01_rooms_and_student_count.txt
│   ├── 02_top_rooms_by_average_age.txt
│   ├── 03_top_rooms_by_age_difference.txt
│   ├── 04_rooms_with_mixed_sex.txt
│   └── 05_optimization_recommendations.txt
└── README.md               # This file
```

### Clean Code Principles

#### One Class Per File
- Each file contains exactly one class
- Clear separation of concerns
- Easy to locate and maintain specific functionality

#### Logical Directory Organization
- **connections/**: Database connection abstractions and implementations
- **protocols/**: Service interfaces and contracts
- **repositories/**: Data access layer implementations
- **queries/**: Business logic query services
- **reports/**: Output formatting and presentation
- **database/**: Database schema and management
- **optimization/**: Performance optimization utilities
- **preview/**: Database preview and inspection tools

#### Direct Imports
- No unnecessary wrapper files
- Direct imports from source modules
- Clear dependency relationships
- No main package `__init__.py` files for services and utils

### SOLID Principles Implementation

#### Single Responsibility Principle (SRP)
- Each class has a single, well-defined responsibility
- `DatabaseConnection`: Only handles database connections
- `MySQLRoomRepository`: Only handles room data operations
- `StudentRoomQueryService`: Only handles student-room queries
- `ConsoleReportGenerator`: Only handles console output formatting

#### Open/Closed Principle (OCP)
- Abstract base classes allow extension without modification
- New database connections can be added by implementing `DatabaseConnection`
- New report formats can be added by implementing `ReportGenerator`
- New repositories can be added by implementing `RoomRepository`/`StudentRepository`

#### Liskov Substitution Principle (LSP)
- Concrete implementations can be substituted for abstract classes
- `MySQLConnection` can be substituted for `DatabaseConnection`
- `ConsoleReportGenerator` can be substituted for `ReportGenerator`
- `MySQLRoomRepository` can be substituted for `RoomRepository`

#### Interface Segregation Principle (ISP)
- Clients depend only on the interfaces they use
- `QueryService` only depends on `DatabaseConnection.fetch_all()`
- `ReportGenerator` only depends on data formatting methods
- `Repository` interfaces are specific to their domain

#### Dependency Inversion Principle (DIP)
- High-level modules don't depend on low-level modules
- `StudentRoomAnalyzer` depends on abstractions, not concrete implementations
- Dependencies are injected through constructors
- All dependencies flow toward abstractions

## 🗄️ Database Schema

### Rooms Table
```sql
CREATE TABLE rooms (
    id INT PRIMARY KEY,
    number VARCHAR(10) NOT NULL,
    building VARCHAR(10) NOT NULL,
    capacity INT NOT NULL,
    INDEX idx_building (building),
    INDEX idx_capacity (capacity)
);
```

### Students Table
```sql
CREATE TABLE students (
    id INT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    sex CHAR(1) NOT NULL,
    room_id INT NOT NULL,
    FOREIGN KEY (room_id) REFERENCES rooms(id),
    INDEX idx_room_id (room_id),
    INDEX idx_age (age),
    INDEX idx_sex (sex),
    INDEX idx_age_sex (age, sex)
);
```

## Query Optimization

### Existing Indexes
- Primary keys on both tables
- Foreign key index on `students.room_id`
- Single-column indexes on frequently queried fields
- Composite index on `students(age, sex)`

### Recommended Additional Indexes
```sql
-- Composite index for age-based room queries
CREATE INDEX idx_students_room_age ON students(room_id, age);

-- Composite index for sex-based room queries
CREATE INDEX idx_students_room_sex ON students(room_id, sex);

-- Composite index for building-based queries
CREATE INDEX idx_rooms_building_number ON rooms(building, number);

-- Covering index for student count queries
CREATE INDEX idx_students_covering ON students(room_id, id);
```

### Performance Features
- All calculations (AVG, MIN, MAX, COUNT) done at database level
- Efficient JOIN operations with proper indexing
- Optimized GROUP BY clauses
- Proper use of HAVING clauses for post-aggregation filtering

## Sample Output

The application generates formatted reports like:

```
ROOMS AND STUDENT COUNT
================================================================================
Room ID    Number     Building   Capacity   Students  
------------------------------------------------------------
101        101        A          2          2         
102        102        A          2          2         
103        103        A          2          2         
...

TOP 5 ROOMS WITH SMALLEST AVERAGE STUDENT AGE
================================================================================
Room ID    Number     Building   Students   Avg Age   
------------------------------------------------------------
107        107        B          2          21.50     
104        104        A          2          21.00     
...
```

## Customization

### Adding New Data Sources
Implement the `DataLoader` interface:

```python
class CustomDataLoader(DataLoader):
    def load_models(self) -> List[YourModel]:
        # Your custom loading logic
        pass
```

### Adding New Report Formats
Implement the `ReportGenerator` interface:

```python
class HTMLReportGenerator(ReportGenerator):
    def format_rooms_with_student_count(self, data: List[Tuple]) -> str:
        # Your HTML formatting logic
        pass
```

### Adding New Queries
Extend the `StudentRoomQueryService` class:

```python
def get_custom_analysis(self) -> List[Tuple]:
    query = "YOUR SQL QUERY HERE"
    return self.execute_query(query)
```

### Adding New Database Connections
Implement the `DatabaseConnection` interface:

```python
class PostgreSQLConnection(DatabaseConnection):
    def connect(self):
        # Your PostgreSQL connection logic
        pass
```

## Troubleshooting

### Common Issues

1. **MySQL Connection Error**
   - Verify MySQL server is running
   - Check credentials in `src/config/config.py`
   - Ensure database user has proper permissions

2. **File Not Found Error**
   - Ensure `students.json` and `rooms.json` exist in the `data/` directory
   - Check file permissions

3. **Import Errors**
   - Run `uv sync` to install dependencies
   - Ensure you're using the virtual environment
   - Check that all `__init__.py` files are present in subdirectories

4. **Module Not Found Errors**
   - Verify the directory structure matches the documentation
   - Check that imports use the correct paths (e.g., `src.services.connections`)
   - Ensure all subdirectories have `__init__.py` files
   - Note: Main package `__init__.py` files are not required for services and utils
