#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

solution = 11111 # Full time works as an int.

def full_time():
    result = 0
    for fp in salary_hourly:
        if fp == 'F':
            result += 1
    print('full-time')
    print(result)
    print()
    return result
