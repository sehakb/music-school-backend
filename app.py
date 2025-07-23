import sqlite3
from flask import Flask, jsonify

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('school.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def home():
    return "Music School API is running."

@app.route("/students")
def get_students():
    conn = get_db_connection()
    students = conn.execute("SELECT * FROM students").fetchall()
    conn.close()
    return jsonify([dict(s) for s in students])

@app.route("/teachers")
def get_teachers():
    conn = get_db_connection()
    teachers = conn.execute("SELECT * FROM teachers").fetchall()
    conn.close()
    return jsonify([dict(t) for t in teachers])

@app.route("/lessons")
def get_lessons():
    conn = get_db_connection()
    lessons = conn.execute("SELECT * FROM lessons").fetchall()
    conn.close()
    return jsonify([dict(l) for l in lessons])

if __name__ == "__main__":
    app.run(debug=True)
