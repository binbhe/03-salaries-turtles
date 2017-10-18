#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

solution = 11223 # Police workers as an int.

def police_number():
    number = 0
    for n in department:
        if 'police' in n.lower():
            number += 1
    print(' policedepartment')
    print(number)
    print()
