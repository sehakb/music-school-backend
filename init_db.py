import sqlite3

def init_db():
    with open('schema.sql', 'r') as f:
        schema = f.read()

    conn = sqlite3.connect('school.db')
    cursor = conn.cursor()
    cursor.executescript(schema)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print(" The database was created successfully.")
