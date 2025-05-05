SELECT DISTINCT sub.subject_name
                FROM Grades g
                JOIN Subjects sub ON g.subject_id = sub.id
                WHERE g.student_id = 1;