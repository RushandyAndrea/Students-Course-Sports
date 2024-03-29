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


def get_list(students):
    """
    Display the all student information stored in a 2nd list, it will notify the user if there is no
    data found.
    :param students: student data (id, first_name, last_name)
    :return: no value
    """
    if len(students) == 0:
        print("There are no student in the database system.\n")
        return

    print(f"{'ID':4s} {'First Name':20s} {'Last Name':20s}")
    print('-' * 4, '-' * 20, '-' * 20)

    for student in students:
        student_id, first_name, last_name, courses, sports = student
        print(f'{student_id:<4d} {first_name:20s} {last_name:20s}', end='')
        print()


def list_student_courses(student):
    """
    Display the selected student course information stored in a 2d list.
    :param student: 2d list of student data [id, first_name, last_name, [courses], [sports]].
    :return: no value
    """
    print(f'Student ID # {student[0]} {student[1]} {student[2]} is in: ', end='')

    for course in student[3]:
        print(f'{course}', end=', ')

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
    Prompt the user to enter a student id, and if not valid return.
    If the student is not in the select course, then display error message
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

    student_id = val.get_poss_num('Please enter the Student ID you would like to be updated: ')
    student_index = find_student_index(students, student_id)

    if student_index == -1:
        print(f'Student ID number {student_id} not found.')
        return

    student = students[student_index]

    confirm = val.get_yes_no(f'Please confirm that you want to update Student ID number '
                             f'{student_id} {student[1]} {student[2]}')

    if confirm:
        updated_first_name = input(f'Please enter the students First Name or press ENTER to keep '
                                   f'{student[1]}: ')
        updated_last_name = input(f'Please enter the students Last Name or press ENTER to keep '
                                  f'{student[2]}: ')

        student[1] = updated_first_name
        student[2] = updated_last_name

    else:
        print(f'Update has been cancelled!')


def get_student_report(students):
    """
    Displays everything that the student is enrolled into.
    :param students:
    :return:
    """
    if len(students) == 0:
        print("There are no student in the database system.\n")
        return

    print(f"{'ID':4s} {'First Name':20s} {'Last Name':20s} {'Sports':25s} {'Courses':25s}")
    print('-' * 4, '-' * 20, '-' * 20, '-' * 25, '-' * 25)

    for student in students:
        student_id, first_name, last_name, courses, sports = student
        print(f'{student_id:<4d} {first_name:20s} {last_name:20s}', end='')

        for sport in sports:
            print(f' {sport}', end=', ')
            for course in courses:
                print(f'                {course}', end=', ')

    return
