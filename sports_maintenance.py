#!/usr/bin/env python3

"""
# Programmer: Rushandy Andrea, Kasey Drevecky
# Date: November 7th, 2021
# Description: For this assignment, we had to work as a team to make a Students course and sports
program that stores list etc.
"""

# Authorship
__author__ = 'Rushandy Andrea, Kasey Drevecky'
__version__ = '1.0'
__date__ = 'November 7th, 2021'
__status__ = 'Development'

import data_validation as val
import student_maintenance as sm


def list_student_sport(students):
    """
    Display the all student information stored in a 2nd list, it will notify the user if there is no
    data found.
    :param students: student data (id, first_name, last_name)
    :return: no value
    """
    if len(students) == 0:
        print("There are no student in the database system.\n")
        return

    print(f"{'ID':4s} {'First Name':20s} {'Last Name':20s} {'Sports':50s}")
    print('-' * 4, '-' * 20, '-' * 20, '-' * 50)

    for student in students:
        student_id, first_name, last_name, courses, sports = student
        print(f'{student_id:<4d} {first_name:20s} {last_name:20s}', end='')

        for sport in sports:
            print(f'{sport}', end=', ')
        print()

    return


def add_student_sport(students, valid_sport):
    """
    Prompt the user to enter a student id, and if not valid return
    Display a list of the courses a student is currently enrolled
    Display a list of valid courses
    Prompt the user to enter a valid course id or 0 to return to the course maintenance menu
    If the student is already in the course, then display error message
    otherwise add the course to the student's course list
    When done, display an update list of all the courses the student is enrolled in
    :param students: multi-dimensional list of student data [[id, first_name, last_name, [courses], [sports]]]
    :param valid_sport: tuple of all valid courses to select from
    :return: no value
    """

    print('Add Sport')
    print('-----------------')

    student_id = val.get_poss_num('Please enter the Student ID you would like to add courses to', 'int')
    student_index = sm.find_student_index(students, student_id)
    if student_index == -1:
        print('Student not found')
        return
    else:
        student = students[student_index]
        print('add course')
        print('=' * 50)
        while True:
            i = 0
            for x in valid_sport:
                i += 1
                print(f'{i} = {x}')
            print('0 = Exit')
            command = val.get_range('Please enter a command number', 0, len(valid_sport))
            if command == 0:
                break
            if valid_sport[command - 1] in student[3]:
                print(f'{student[1]} is already in {valid_sport[command - 1]}')
            else:
                student[4].append(valid_sport[command - 1])
                print(f'{student[1]} has been added to {valid_sport[command - 1]}')


def delete_student_sport(students):
    """
    Prompt the user to enter a student id, and if not valid return
    Prompt the user to enter a student id, and if not valid return
    Display a list of valid courses
    Prompt the user to enter a valid course id or 0 to return to the course maintenance menu
    If the student is not the select course, then display error message
    otherwise remove the course to the student's course list
    When done, display an update list of all the courses the student is enrolled in
    :param students: multi-dimensional list of student data [[id, first_name, last_name, [courses], [sports]]]
    :return: no value
    """
    if len(students) == 0:
        print('There are no students in the database. \n')
        return

    student_id = val.get_poss_num('Please enter the Student ID you would like to add courses to', 'int')
    student_index = sm.find_student_index(students, student_id)
    if student_index == -1:
        print('Student not found')
        return
    else:
        student = students[student_index]
        print('Delete Course')
        print('=' * 50)
        while True:
            i = 0
            for x in student[4]:
                i += 1
                print(f'{i} = {x}')
            print('0 = Exit')
            command = val.get_range('Please enter a command number', 0, len(student[3]))
            if command == 0:
                break
            else:
                print(f'{student[1]} has been removed from {student[4].pop(command - 1)}')
