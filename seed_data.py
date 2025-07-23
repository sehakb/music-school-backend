import sqlite3
from datetime import date

conn = sqlite3.connect('school.db')
cursor = conn.cursor()

# Öğretmen ekle
cursor.execute("INSERT INTO teachers (name) VALUES (?)", ("Kerem Toprak",))
teacher_id = cursor.lastrowid

# Öğrenci ekle
cursor.execute("""
    INSERT INTO students (full_name, instrument, phone, status, teacher_id, registration_date)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("Ahmet Bakır", "Piano", "555-1234", "active", teacher_id, date.today().isoformat()))

cursor.execute("""
    INSERT INTO students (full_name, instrument, phone, status, teacher_id, registration_date)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("Emre Koçak", "Drums", "555-5678", "active", teacher_id, date.today().isoformat()))

conn.commit()
conn.close()

print("Test data added.")
