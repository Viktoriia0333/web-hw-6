from faker import Faker
import random
from datetime import datetime, timedelta
from create_db import cursor, conn

fake = Faker()


# Заповнення таблиці груп
def fill():
    groups = ['Group A', 'Group B', 'Group C']
    for group in groups:
        cursor.execute("INSERT INTO Groups (group_name) VALUES (?)", (group,))

    # Заповнення таблиці викладачів
    teachers = []
    for _ in range(5):  # 5 викладачів
        teachers.append((fake.first_name(), fake.last_name()))
    cursor.executemany("INSERT INTO Teachers (first_name, last_name) VALUES (?, ?)", teachers)

    # Заповнення таблиці студентів
    students = []
    for _ in range(30):  # 30 студентів
        group_id = random.choice([1, 2, 3])  # Вибір групи
        students.append((fake.first_name(), fake.last_name(), group_id))
    cursor.executemany("INSERT INTO Students (first_name, last_name, group_id) VALUES (?, ?, ?)", students)

    # Заповнення таблиці предметів
    subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 'Computer Science', 'History', 'Geography']
    subject_teacher_mapping = []
    for subject in subjects:
        teacher_id = random.randint(1, 5)  # Вибір викладача
        subject_teacher_mapping.append((subject, teacher_id))
    cursor.executemany("INSERT INTO Subjects (subject_name, teacher_id) VALUES (?, ?)", subject_teacher_mapping)

    # Заповнення таблиці оцінок
    grades = []
    for student_id in range(1, 31):  # Для кожного студента
        for subject_id in range(1, 8):  # Для кожного предмета
            grade = round(random.uniform(1.0, 5.0), 2)  # Випадкова оцінка
            grade_date = fake.date_this_year()  # Випадкова дата
            grades.append((student_id, subject_id, grade, grade_date))

    cursor.executemany("INSERT INTO Grades (student_id, subject_id, grade, grade_date) VALUES (?, ?, ?, ?)", grades)

    # Підтвердження змін
    conn.commit()


