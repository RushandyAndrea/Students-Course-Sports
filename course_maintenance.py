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


def add_course(students, valid_courses):
    print('Add Courses')
    print('=' * 50)
    student_id = val.get_poss_num('Please enter the Student ID you would like to add courses to', 'int')
    student_index = sm.find_student_index(students, student_id)
    if student_index == -1:
        print('Student not found')
        return
    else:
        student = students[student_index]
        print('Add Course')
        print('=' * 50)
        while True:
            i = 0
            for x in valid_courses:
                i += 1
                print(f'{i} = {x}')
            print('0 = Exit')
            command = val.get_range('Please enter a command number', 0, len(valid_courses))
            if command == 0:
                break
            if valid_courses[command - 1] in student[3]:
                print(f'{student[1]} is already enrolled in {valid_courses[command - 1]}')
            else:
                student[3].append(valid_courses[command - 1])
                print(f'{student[1]} has been enrolled in {valid_courses[command - 1]}')


def delete_course(students):
    print('Delete Courses')
    print('=' * 50)
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
            for x in student[3]:
                i += 1
                print(f'{i} = {x}')
            print('0 = Exit')
            command = val.get_range('Please enter a command number', 0, len(student[3]))
            if command == 0:
                break
            else:
                print(f'{student[1]} has been removed from {student[3].pop(command - 1)}')

