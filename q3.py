#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

solution = 1234 # Part-time as an int.

def part_time():
    result = 0
    for fp in salary_hourly:
        if fp == 'P':
            result += 1
    if result == (employee_number() - full_time()):
        print('第三题')
        print('ok')
        print(result)
        print()
    else:
        print('no')
