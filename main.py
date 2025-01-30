from Task_1 import *

if is_student_empty() and is_room_empty():
    paths = []
    print('Enter path to students file:')
    paths.append(input())
    print('Enter path to rooms file:')
    paths.append(input())
    primary_process(paths, [query_0_1, query_0_2])

print('In which way would you like to save data? (json/xml)')
file_format = input()
flag, result = 'y', []
while flag == 'y':
    print('Enter number of query you want to run:')
    print('1 : List of rooms and the number of students in each of them')
    print('2 : 5 rooms with the lowest average age of students')
    print('3 : 5 rooms with the largest age difference among students')
    print('4 : List of rooms where M and F students live')
    dop = input()
    if dop == '1':
        result = prompt_1()
    elif dop == '2':
        result = prompt_2()
    elif dop == '3':
        result = prompt_3()
    elif dop == '4':
        result = prompt_4()
    else:
        print('Invalid input')

    print('Enter name of file to save data:')
    file_name = input()
    if file_format == 'json':
        write_result_json(file_name, result, int(dop))
    elif file_format == 'xml':
        write_result_xml(file_name, result, int(dop))
    else:
        print('File format not supported')
    print('Do you want to continue (y/n)')
    flag = input()
