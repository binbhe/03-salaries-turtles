#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

solution = 1123 # Detectives as int.

def detectives_number():
    number = 0
    for n in department:
        if 'detective' in n.lower():
            number += 1
    print('detectives')
    print(number)
    print()
