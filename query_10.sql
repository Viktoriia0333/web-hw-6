SELECT sub.subject_name
                FROM Subjects sub
                JOIN Grades g ON sub.id = g.subject_id
                WHERE g.student_id = 1 AND sub.teacher_id = 1;