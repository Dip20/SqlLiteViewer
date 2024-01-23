import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('main_database.db')
cursor = conn.cursor()

# Insert sample data into students table
cursor.executemany('''
    INSERT INTO students (first_name, last_name, email)
    VALUES (?, ?, ?)
''', [
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Alice', 'Johnson', 'alice.johnson@example.com'),
    ('Bob', 'Williams', 'bob.williams@example.com')
])

# Commit changes to the students table
conn.commit()

# Insert sample attendance data
cursor.executemany('''
    INSERT INTO attendance (student_id, attendance_date, status)
    VALUES (?, ?, ?)
''', [
    (1, '2022-01-01', 'Present'),
    (2, '2022-01-01', 'Absent'),
    (3, '2022-01-01', 'Present'),
    (4, '2022-01-01', 'Absent'),
    (1, '2022-01-02', 'Present'),
    (2, '2022-01-02', 'Present'),
    (3, '2022-01-02', 'Absent'),
    (4, '2022-01-02', 'Absent')
])

# Commit changes to the attendance table
conn.commit()



# Insert sample attendance data
cursor.executemany('''
    INSERT INTO orders (id, product_id, qty, created_at)
        VALUES (?, ?, ?, ?)
''', [
    (101, 1, 5, '2022-01-01 10:30:00'),
    (102, 2, 3, '2022-01-02 12:45:00'),
    (103, 1, 2, '2022-01-03 15:20:00'),
    (104, 3, 8, '2022-01-04 08:10:00'),
    (105, 2, 4, '2022-01-05 14:00:00')
])

# Commit changes to the attendance table
conn.commit()

# Close connection
conn.close()

print("Sample data inserted successfully.")
