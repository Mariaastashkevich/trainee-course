query_0_1 = '''
            INSERT INTO Student (birthday, id, name, room, sex) VALUES (%s, %s, %s, %s, %s)
            '''
query_0_2 = '''
            INSERT INTO Room (name) VALUES (%s)
            '''
query_1 = '''
    select Room.name, COUNT(Student.id) as StudentsCount from Room
    left join Student on Room.name = Student.room
    group by Room.name
    ORDER BY CAST(Room.name AS UNSIGNED);
    '''
query_2 = '''
    SELECT room, AVG(YEAR(CURDATE()) - YEAR(birthday) - (DATE_FORMAT(CURDATE(), '%m%d') < DATE_FORMAT(birthday, '%m%d'))) AS average_age
    FROM Student
    GROUP BY room
    order by average_age
    limit 5;
'''
query_3 = '''
    SELECT room, MAX(YEAR(CURDATE()) - YEAR(birthday) - (DATE_FORMAT(CURDATE(), '%m%d') < DATE_FORMAT(birthday, '%m%d'))) - MIN(YEAR(CURDATE()) - YEAR(birthday) - (DATE_FORMAT(CURDATE(), '%m%d') < DATE_FORMAT(birthday, '%m%d'))) AS age_difference
    FROM Student
    group by room
    order by age_difference DESC
    limit 5;
    '''
query_4 = '''
    SELECT room, COUNT(DISTINCT sex) AS gender_count
    FROM Student
    GROUP BY room
    HAVING gender_count = 2;
    '''
query_is_empty_student = '''
SELECT 
    CASE 
        WHEN EXISTS (SELECT 1 FROM Student) 
            THEN 0 
        ELSE 1 
    END AS IsEmpty;
'''
query_is_empty_room = '''
SELECT 
    CASE 
        WHEN EXISTS (SELECT 1 FROM Room) 
            THEN 0 
        ELSE 1 
    END AS IsEmpty;
'''
