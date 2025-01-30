import re

import xml.etree.ElementTree as ET
import mysql.connector
import json
from queries import *
import pandas as pd


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
    res_1, res_2 = [], []
    for row in results:
        res_1.append(row[0])
        res_2.append(row[1])
        print(f"Room Number: {row[0]}, Number of students: {row[1]}")

    connection.commit()
    cursor.close()
    connection.close()
    return res_1, res_2


def prompt_2():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_2)
    results = cursor.fetchall()
    res_1, res_2 = [], []
    for row in results:
        res_1.append(row[0])
        res_2.append(row[1])
        print(f"Room Number: {row[0]}, Average age: {row[1]}")
    connection.commit()
    cursor.close()
    connection.close()
    return res_1, res_2


def prompt_3():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_3)
    results = cursor.fetchall()
    res_1, res_2 = [], []
    for row in results:
        res_1.append(row[0])
        res_2.append(row[1])
        print(f"Room Number: {row[0]}, Age difference: {row[1]}")
    connection.commit()
    cursor.close()
    connection.close()
    return res_1, res_2


def prompt_4():
    connection = connect_to_db()
    cursor = connection.cursor()
    cursor.execute(query_4)
    results = cursor.fetchall()
    res_1 = []
    print('Rooms with M and F gender:')
    for row in results:
        res_1.append(row[0])
        print(f"Room Number: {row[0]}")
    connection.commit()
    cursor.close()
    connection.close()
    return res_1


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


def write_result_json(file_name, result, prompt):
    if prompt == 1:
        data = {
            "Room number": result[0],
            "Number of students": result[1]
        }
    elif prompt == 2:
        data = {
            "Room number": result[0],
            "Average age": result[1]
        }
    elif prompt == 3:
        data = {
            "Room number": result[0],
            "Age difference": result[1]
        }
    elif prompt == 4:
        data = {
            "Room number": result
        }
    df = pd.DataFrame(data)
    df.to_json(file_name, orient="records", lines=False)


def write_result_xml(file_name, result, prompt):
    root = ET.Element("rooms")
    if prompt == 1:
        for room_number, avg_age in zip(result[0], result[1]):
            room = ET.SubElement(root, "room")
            room_number_elem = ET.SubElement(room, "RoomNumber")
            room_number_elem.text = str(room_number)
            number_of_students_elem = ET.SubElement(room, "NumberOfStudents")
            number_of_students_elem.text = str(avg_age)
    elif prompt == 2:
        root = ET.Element("rooms")
        for room_number, avg_age in zip(result[0], result[1]):
            room = ET.SubElement(root, "room")
            room_number_elem = ET.SubElement(room, "RoomNumber")
            room_number_elem.text = str(room_number)
            number_of_students_elem = ET.SubElement(room, "AverageAge")
            number_of_students_elem.text = str(avg_age)
    elif prompt == 3:
        root = ET.Element("rooms")
        for room_number, age_diff in zip(result[0], result[1]):
            room = ET.SubElement(root, "room")
            room_number_elem = ET.SubElement(room, "RoomNumber")
            room_number_elem.text = str(room_number)
            number_of_students_elem = ET.SubElement(room, "AgeDifference")
            number_of_students_elem.text = str(age_diff)
    elif prompt == 4:
        root = ET.Element("rooms")
        for room_number in zip(result):
            room = ET.SubElement(root, "room")
            room_number_elem = ET.SubElement(room, "RoomNumber")
            room_number_elem.text = str(room_number)

    tree = ET.ElementTree(root)
    tree.write(file_name, encoding='utf-8', xml_declaration=True)
