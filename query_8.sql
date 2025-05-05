SELECT AVG(g.grade) AS avg_grade
                FROM Grades g
                JOIN Subjects s ON g.subject_id = s.id
                WHERE s.teacher_id = 1;