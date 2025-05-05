SELECT gr.group_name, AVG(g.grade) AS avg_grade
                FROM Groups gr
                JOIN Students s ON gr.id = s.group_id
                JOIN Grades g ON s.id = g.student_id
                WHERE g.subject_id = 1
                GROUP BY gr.id;