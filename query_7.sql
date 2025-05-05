SELECT s.first_name, s.last_name, g.grade
                FROM Students s
                JOIN Grades g ON s.id = g.student_id
                WHERE s.group_id = 1 AND g.subject_id = 1;