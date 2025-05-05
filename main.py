from create_db import conn, cursor, create_tables
import fill_db


def main():
    create_tables()
    fill_db.fill()


def get_queries():
    queries = {
        1: '''
                SELECT s.first_name, s.last_name, AVG(g.grade) AS avg_grade
                FROM Students s
                JOIN Grades g ON s.id = g.student_id
                GROUP BY s.id
                ORDER BY avg_grade DESC
                LIMIT 5;
            ''',
        2: '''
                SELECT s.first_name, s.last_name, AVG(g.grade) AS avg_grade
                FROM Students s
                JOIN Grades g ON s.id = g.student_id
                WHERE g.subject_id = 1
                GROUP BY s.id
                ORDER BY avg_grade DESC
                LIMIT 1;
            ''',
        3: '''
                SELECT gr.group_name, AVG(g.grade) AS avg_grade
                FROM Groups gr
                JOIN Students s ON gr.id = s.group_id
                JOIN Grades g ON s.id = g.student_id
                WHERE g.subject_id = 1
                GROUP BY gr.id;
            ''',
        4: '''
                SELECT AVG(grade) AS avg_grade
                FROM Grades;
            ''',
        5: '''
                SELECT subject_name
                FROM Subjects
                WHERE teacher_id = 1;
            ''',
        6: '''
                SELECT s.first_name, s.last_name
                FROM Students s
                WHERE s.group_id = 1;
            ''',
        7: '''
                SELECT s.first_name, s.last_name, g.grade
                FROM Students s
                JOIN Grades g ON s.id = g.student_id
                WHERE s.group_id = 1 AND g.subject_id = 1;
            ''',
        8: '''
                SELECT AVG(g.grade) AS avg_grade
                FROM Grades g
                JOIN Subjects s ON g.subject_id = s.id
                WHERE s.teacher_id = 1;
            ''',
        9: '''
                SELECT DISTINCT sub.subject_name
                FROM Grades g
                JOIN Subjects sub ON g.subject_id = sub.id
                WHERE g.student_id = 1;
            ''',
        10: '''
                SELECT sub.subject_name
                FROM Subjects sub
                JOIN Grades g ON sub.id = g.subject_id
                WHERE g.student_id = 1 AND sub.teacher_id = 1;
            '''
    }

    for num, query in queries.items():
        with open(f'query_{num}.sql', 'w', encoding='utf-8') as f:
            f.write(query.strip())
        print(f'\n--- Query {num} Result ---')
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(f'Error in query {num}: {e}')

    conn.close()


if __name__ == '__main__':
    main()
    get_queries()