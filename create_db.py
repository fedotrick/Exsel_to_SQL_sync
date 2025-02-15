import sqlite3
import os

def create_database():
    # Remove existing database if it exists
    if os.path.exists('plavka.db'):
        os.remove('plavka.db')
    
    # Create new database connection
    conn = sqlite3.connect('plavka.db')
    cursor = conn.cursor()
    
    # Enable foreign key support
    cursor.execute('PRAGMA foreign_keys = ON')
    
    # Create plavki table
    cursor.execute("""
    CREATE TABLE plavki (
        id TEXT PRIMARY KEY,
        uchet_number TEXT,
        date DATE,
        plavka_number TEXT NOT NULL,
        cluster_number TEXT,
        senior_shift TEXT,
        participant1 TEXT,
        participant2 TEXT,
        participant3 TEXT,
        participant4 TEXT,
        casting_name TEXT,
        experiment_type TEXT,
        comment TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    
    # Create sectors table
    cursor.execute("""
    CREATE TABLE sectors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        plavka_id TEXT,
        sector_name TEXT,
        sector_number INTEGER,
        heating_time TIME,
        movement_time TIME,
        pouring_time TIME,
        temperature REAL,
        FOREIGN KEY (plavka_id) REFERENCES plavki (id),
        UNIQUE(plavka_id, sector_name)
    )
    """)
    
    # Commit changes and close connection
    conn.commit()
    conn.close()
    
    print("Database created successfully!")

if __name__ == "__main__":
    create_database()
