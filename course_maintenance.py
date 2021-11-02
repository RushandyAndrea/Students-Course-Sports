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
    student_index = sm.find_student_index(students,student_id)
    if student_index == -1:
        print('Student not found')
        return
    else:
        print('add course')
