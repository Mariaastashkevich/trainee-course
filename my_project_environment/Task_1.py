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
        cursor.execute(query_list[0],
                       (student['birthday'], student['id'], student['name'], student['room'], student['sex']))

    for room in rooms_data:
        cursor.execute(query_list[1], (re.findall(r'\b\d{1,3}\b', room['name'])[0],))
    connection.commit()
    cursor.close()
    connection.close()


def prompt_1():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_1)
    results = cursor.fetchall()
    for row in results:
        print(f"Room Number: {row[0]}, Number of students: {row[1]}")
    connection.commit()
    cursor.close()
    connection.close()


def prompt_2():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_2)
    results = cursor.fetchall()
    for row in results:
        print(f"Room Number: {row[0]}, Average age: {row[1]}")
    connection.commit()
    cursor.close()
    connection.close()


def prompt_3():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_3)
    results = cursor.fetchall()
    for row in results:
        print(f"Room Number: {row[0]}, Age difference: {row[1]}")
    connection.commit()
    cursor.close()
    connection.close()


def prompt_4():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_4)
    results = cursor.fetchall()
    print('Rooms with M and F gender:')
    for row in results:
        print(f"Room Number: {row[0]}")
    connection.commit()
    cursor.close()
    connection.close()


def is_student_empty():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_is_empty_student)
    results = cursor.fetchall()
    if results[0][0] == 0:
        return False
    else:
        return True


def is_room_empty():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_is_empty_room)
    results = cursor.fetchall()
    if results[0][0] == 0:
        return False
    else:
        return True
