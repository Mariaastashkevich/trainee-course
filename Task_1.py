import re
import mysql.connector
import json
from queries import *


def connect_to_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='Myloveisme2611',
        database='Students'
    )


def primary_process(file_name, query_list):
    connection = connect_to_db()
    cursor = connection.cursor()

    with open(file_name[0]) as json_file:
        students_data = json.load(json_file)
    with open(file_name[1]) as json_file:
        rooms_data = json.load(json_file)

    cursor = connection.cursor()
    for student in students_data:
        cursor.execute(query_list[0], (student['birthday'], student['id'], student['name'], student['room'], student['sex']))

    for room in rooms_data:
        cursor.execute(query_list[1], (re.findall(r'\b\d{1,3}\b', room['name'])[0],))
    connection.commit()
    cursor.close()
    connection.close()


def secondary_process(query_list):
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_list[0])
    cursor.execute(query_list[1])
    cursor.execute(query_list[2])
    cursor.execute(query_list[3])
    student_results = cursor.fetchall()
    cursor.execute(query_list[4])
    results = cursor.fetchall()
    for row in results:
        print(f"Room Number: {row[1]}, Number of students: {row[2]}")

    cursor.execute(query_list[5])
    cursor.execute(query_list[6])
    cursor.execute(query_list[7])
    results = cursor.fetchall()
    for row in results:
        print(f"Room ID: {row[0]}, Room Number: {row[1]}, Average age: {row[2]}")

    cursor.execute(query_list[8])
    results = cursor.fetchall()
    for row in results:
        print(f"Room Number: {row[0]}, Age difference: {row[1]}")

    cursor.execute(query_list[9])
    results = cursor.fetchall()
    print('Rooms with M and F gender:')
    for row in results:
        print(f"Room Number: {row[0]}")
    connection.commit()
    cursor.close()
    connection.close()


primary_process(['students.json', 'rooms.json'], [query_0_1, query_0_2])
secondary_process(
    [query_1_1, query_1_2, query_1_3, query_1_4, query_1_5, query_2_1, query_2_2, query_2_3, query_3_1, query_4_1])

