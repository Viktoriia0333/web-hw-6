SELECT s.first_name, s.last_name, AVG(g.grade) AS avg_grade
                FROM Students s
                JOIN Grades g ON s.id = g.student_id
                WHERE g.subject_id = 1
                GROUP BY s.id
                ORDER BY avg_grade DESC
                LIMIT 1;