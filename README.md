# Music School Scheduling API

This is a backend API project built with Flask and SQLite for managing students, teachers, and lesson schedules in a music school context.

## 🔧 Features

- Add and list students with instruments, status, and assigned teachers
- Manage teachers
- Track lesson sessions with date and trial flag
- Trial lessons supported
- Ready for containerization and CI/CD

## 📁 Tech Stack

- Python 3
- Flask
- SQLite
- Flask-SQLAlchemy
- Git / GitHub

## 🚀 How to Run Locally

1. Clone the repository  
   `git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git`

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install flask flask_sqlalchemy
   ```

4. Create the database:
   ```bash
   python init_db.py
   python seed_data.py
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. Open in browser:
   - Students: `http://127.0.0.1:5000/students`
   - Teachers: `http://127.0.0.1:5000/teachers`
   - Lessons: `http://127.0.0.1:5000/lessons`
