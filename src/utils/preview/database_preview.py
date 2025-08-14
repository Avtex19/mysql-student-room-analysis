#!/usr/bin/env python3
"""
Database Preview Script - Shows database structure and sample data.
"""

import json


class DatabasePreview:
    """Preview of the database structure and data."""
    
    def __init__(self):
        self.students_data = []
        self.rooms_data = []
        self.load_data()
    
    def load_data(self):
        """Load data from JSON files."""
        try:
            with open('data/students.json', 'r') as f:
                self.students_data = json.load(f)
            with open('data/rooms.json', 'r') as f:
                self.rooms_data = json.load(f)
        except Exception as e:
            print(f"Error loading data: {e}")
    
    def show_summary(self):
        """Show database summary."""
        print(f"Database Summary: {len(self.students_data)} students, {len(self.rooms_data)} rooms")
        
        ages = [s['age'] for s in self.students_data]
        male_count = len([s for s in self.students_data if s['sex'] == 'M'])
        female_count = len([s for s in self.students_data if s['sex'] == 'F'])
        
        print(f"   Average age: {sum(ages) / len(ages):.1f}")
        print(f"   Gender: {male_count}M, {female_count}F")
        
        room_occupancy = {}
        for student in self.students_data:
            room_id = student['room_id']
            room_occupancy[room_id] = room_occupancy.get(room_id, 0) + 1
        
        print(f"   Occupied rooms: {len(room_occupancy)}/{len(self.rooms_data)}")
    
    def show_sample_data(self, limit=3):
        """Show sample data."""
        print(f"\nSample Data (first {limit} records):")
        print("Rooms:", self.rooms_data[:limit])
        print("Students:", self.students_data[:limit])
    
    def show_schema(self):
        """Show database schema."""
        print("\nDatabase Schema:")
        print("rooms: id, number, building, capacity")
        print("students: id, name, age, sex, room_id")
        print("Relationship: students.room_id → rooms.id (Many-to-One)")
    
    def run(self):
        """Run the preview."""
        print("DATABASE PREVIEW")
        print("=" * 40)
        self.show_schema()
        self.show_summary()
        self.show_sample_data()
        print("\nPreview complete!")


def main():
    """Main function."""
    preview = DatabasePreview()
    preview.run()


if __name__ == "__main__":
    main()
