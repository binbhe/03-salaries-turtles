#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

solution = 89012.34 # Median salary as a float (note, different from HW)

def fire_median():
    fire_annual_salary = zip(full_part_time, annual_salary)
    fire_money = []
    for fire, money in fire_annual_salary:
        if fire.lower() == 'fire':
            fire_money.append(money)
    num = len(fire_money)
    count = 0
    for money in fire_money:
        count += 1
        if count > num // 2:
            print('medianfireperson')
            print(money)
            print()
            break
