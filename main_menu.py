#!/usr/bin/env python3

"""
# Programmer: Rushandy Andrea
# Date: October 31, 2021
# Description: For this assignment, I have to create a program that will store student's ID's
, plus first and last name in a tow-dimensional list.
"""

# Authorship
__author__ = 'Rushandy Andrea'
__version__ = '1.0'
__date__ = 'Oct 31, 2021'
__status__ = 'Development'

import student_maintenance as sm
import data_validation as val


def display_menu():
    print('COMMAND MENU')
    print('1 - List all students')
    print('2 - Add a student')
    print('3 - Update a student')
    print('4 - Delete a student')
    print('0 - Exit program')
    print()


def main():
    students = []
    next_student_id = 1

    while True:
        display_menu()
        command = val.get_range('Please enter a command number', 0, 4)
        print()

        if command == 1:
            sm.get_list(students)
        elif command == 2:
            sm.add_student(students, next_student_id)
        elif command == 3:
            sm.update_student(students)
        elif command == 4:
            sm.delete(students)
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
