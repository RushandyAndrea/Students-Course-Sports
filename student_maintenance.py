#!/usr/bin/env python3

"""
# Programmer: Rushandy Andrea
# Date: October 31, 2021
# Description: This module contains the functions for adding, updating, and deleting student data.
"""

# Authorship
__author__ = 'Rushandy Andrea'
__version__ = '1.0'
__date__ = 'Oct 31, 2021'
__status__ = 'Development'

import data_validation as val


def get_list(students):
    """
    Display the all student information stored in a 2nd list, it will notify the user if there is no
    data found.
    :param students: student data (id, first_name, last_name)
    :return:
    """
    if len(students) == 0:
        print("There are no student in the database system.\n")
        return

    print(f"{'ID':4s} {'First Name':20s} {'Last Name':20s}")
    print('-' * 4, '-' * 20, '-' * 20)

    for student in students:
        print(f'{student[0]:<4d} {student[1]:20s} {student[2]:20s}')
    print()


def add_student(students, next_student_id):
    """
    Display the all student information stored in a 2D list.  It will increment the last student id by one
    and use it as the new student's id.  It also, displays that the student was successfully added.
    :param students: student data (id, first_name, last_name)
    :type students: 2d list
    :param next_student_id: the next student id to be used for the add function
    :return: no value
    :rtype: none

    """

    print('Add Student')
    print('-----------------')

    student_first_name = val.get_string('First name of student: ').title()
    student_last_name = val.get_string('Last name of student: ').title()
    course_list = []
    sports_list = []

    students.append([next_student_id, student_first_name, student_last_name, course_list, sports_list])

    print(f'Student ID number {next_student_id} {student_first_name} {student_last_name} was added.')


def delete(students):
    """

    :param students:
    :return:
    """
    if len(students) == 0:
        print('There are no students in the database. \n')
        return

    student_id = val.get_poss_num('Please enter the Student ID you would like to delete')

    student_index = find_student_index(students, student_id)

    if student_index == -1:
        print(f'Student ID number{student_id} not found.')
        return

    student = students[student_index]

    confirm = val.get_yes_no(f'Please confirm that you want to delete Student ID number'
                             f'{student_id} {student[1]} {student[2]}')

    if confirm:
        student = students.pop(student_index)
        print(f'Student ID number{student_id} {student[1]} {student[2]} was deleted')
    else:
        print(f'Deleted was cancelled!')


def find_student_index(students, student_id):
    """
    Search the 2D list for a specific student ID.
    :param students: students: student data (id, first_name, last_name)
    :param student_id: student id that the user wants to find.
    :return: -1 if not found or the index of the student in the 2D list.
    """
    for student in students:
        if student_id == student[0]:
            return students.index(student)
    return -1


def update_student(students):
    """
    This will first check to see if there is any student data, and notify the user if no data is found.
    :param students:
    :return:
    """

    if len(students) == 0:
        print('There are no students in the database. \n')
        return

    student_id = val.get_poss_num('Please enter the Student ID you would like to updated: ')

    first_name = students[student_id][1]
    last_name = students[student_id][2]

    if student_id == -1:
        print(f'Student ID number{student_id} not found.')
        return

    student = students[student_id]

    confirm = val.get_yes_no(f'Please confirm that you want to update Student ID number'
                             f'{student_id} {student[1]} {student[2]}')

    if confirm in ['y', 'yes']:
        updated_first_name = input(f'Please enter the students First Name or press ENTER to keep '
                                   f'{student[1]}: ')
        updated_last_name = input(f'Please enter the students Last Name or press ENTER to keep'
                                  f'{student[2]}: ')

        student[student_id][1] = updated_first_name
        student[student_id][2] = updated_last_name

    else:
        print(f'Update has been cancelled!')
