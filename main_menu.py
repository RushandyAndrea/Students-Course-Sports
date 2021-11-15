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

import student_maintenance as sm
import data_validation as val
import course_maintenance as cm
import sports_maintenance as spm


def display_menu():
    print('COMMAND MENU')
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('5 - Update Student Course List')
    print('6 - Update Student Sports List')
    print('7 - Student Records Report')
    print('0 - Exit program')
    print()


def display_course_menu():
    print('COMMAND MENU')
    print('1 - List Student Courses')
    print('2 - Add Course')
    print('3 - Delete Course')
    print('0 - Back')


def display_sports_menu():
    print('COMMAND MENU')
    print('1 - List Student Sports')
    print('2 - Add Sport')
    print('3 - Delete Sports')
    print('0 - Back')


def main():
    students = []
    valid_courses = ('History', 'Math', 'English', 'Spanish', 'Programming', 'Psychology')
    valid_sports = ('Football', 'Baseball', 'Basketball', 'Track', 'Soccer', 'Swimming')
    next_student_id = 1

    while True:
        display_menu()
        command = val.get_range('Please enter a command number', 0, 7)
        print()
        if command == 1:
            sm.get_list(students)
        elif command == 2:
            sm.add_student(students, next_student_id)
            next_student_id += 1
        elif command == 3:
            sm.update_student(students)
        elif command == 4:
            sm.delete(students)
        elif command == 5:
            display_course_menu()
            command = val.get_range('Please enter a command number', 0, 3)
            if command == 1:
                cm.list_student_course(students)
            elif command == 2:
                cm.add_course(students, valid_courses)
            elif command == 3:
                cm.delete_course(students)
            elif command == 0:
                break
        elif command == 6:
            display_sports_menu()
            command = val.get_range('Please enter a command number', 0, 3)
            if command == 1:
                spm.list_student_sport(students)
            elif command == 2:
                spm.add_student_sport(students, valid_sports)
            elif command == 3:
                spm.delete_student_sport(students)
            elif command == 0:
                break
        elif command == 7:
            sm.get_student_report(students)
        elif command == 0:
            break
        else:
            print("Not a valid command. Please try again.\n")

        print()
        input('Press the enter key to continue...')
        print()

    print("Bye!")


if __name__ == "__main__":
    main()
