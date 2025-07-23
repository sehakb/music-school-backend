DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS lessons;

CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    instrument TEXT NOT NULL,
    phone TEXT,
    status TEXT CHECK(status IN ('active', 'inactive')) NOT NULL,
    teacher_id INTEGER,
    registration_date TEXT NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);

CREATE TABLE lessons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    teacher_id INTEGER,
    date TEXT NOT NULL,
    is_trial BOOLEAN NOT NULL DEFAULT 0,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);
