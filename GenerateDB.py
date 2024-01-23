import sqlite3

# Connect to SQLite database (creates a new database if it doesn't exist)
conn = sqlite3.connect('main_database.db')
cursor = conn.cursor()

# Create students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL
    )
''')

# Create attendance table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        attendance_id INTEGER PRIMARY KEY,
        student_id INTEGER,
        attendance_date DATE NOT NULL,
        status TEXT NOT NULL CHECK (status IN ('Present', 'Absent')),
        FOREIGN KEY (student_id) REFERENCES students(student_id)
    )
''')

# Create attendance table
cursor.execute('''
    CREATE TABLE orders (
        order_id INTEGER PRIMARY KEY,
        id INTEGER,
        product_id INTEGER,
        qty INTEGER,
        created_at DATETIME
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()

print("Database and tables created successfully.")
