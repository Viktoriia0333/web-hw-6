import sqlite3

# Створення підключення до бази даних SQLite
conn = sqlite3.connect('university1.db')
cursor = conn.cursor()


def create_tables():
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT,
                        group_id INTEGER)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Groups (
                        id INTEGER PRIMARY KEY,
                        group_name TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Teachers (
                        id INTEGER PRIMARY KEY,
                        first_name TEXT,
                        last_name TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Subjects (
                        id INTEGER PRIMARY KEY,
                        subject_name TEXT,
                        teacher_id INTEGER,
                        FOREIGN KEY(teacher_id) REFERENCES Teachers(id))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Grades (
                        id INTEGER PRIMARY KEY,
                        student_id INTEGER,
                        subject_id INTEGER,
                        grade REAL,
                        grade_date DATE,
                        FOREIGN KEY(student_id) REFERENCES Students(id),
                        FOREIGN KEY(subject_id) REFERENCES Subjects(id))''')

    conn.commit()
