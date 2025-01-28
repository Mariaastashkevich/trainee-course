query_0_1 = '''
            INSERT INTO Student (birthday, id, name, room, sex) VALUES (%s, %s, %s, %s, %s)
            '''
query_0_2 = '''
            INSERT INTO Room (name) VALUES (%s)
            '''
query_1_1 = 'ALTER TABLE Student ADD room_id INT;'
query_1_2 = '''
    ALTER TABLE Student
    ADD CONSTRAINT fk_room
    FOREIGN KEY (room_id) REFERENCES Room(id);
    '''
query_1_3 = '''
    UPDATE Student s
    JOIN Room r ON s.room = r.name
    SET s.room_id = r.id;
    '''
query_1_4 = 'SELECT * FROM Student ORDER BY room_id;'
query_1_5 = '''
    SELECT Room.id, Room.name, COUNT(Student.id) AS StudentsCount
    FROM Room
    LEFT JOIN Student ON Room.id = Student.room_id
    GROUP BY Room.id, Room.name
    ORDER BY CAST(Room.name AS UNSIGNED);
    '''
query_2_1 = 'ALTER TABLE Student ADD COLUMN age INT;'
query_2_2 = '''
UPDATE Student
SET age = YEAR(CURDATE()) - YEAR(birthday) - (DATE_FORMAT(CURDATE(), '%m%d') < DATE_FORMAT(birthday, '%m%d'));
'''
query_2_3 = '''
SELECT room_id, room, AVG(age) AS average_age
FROM Student
GROUP BY room_id, room
order by AVG(age)
limit 5;
'''
query_3_1 = '''
    SELECT room, MAX(age) - MIN(age) AS age_difference
    FROM Student
    group by room
    order by MAX(age) - MIN(age) DESC
    limit 5;
    '''
query_4_1 = '''
    SELECT room, COUNT(DISTINCT sex) AS gender_count
    FROM Student
    GROUP BY room
    HAVING gender_count = 2;
    '''
