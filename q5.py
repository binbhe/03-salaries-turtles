#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

solution = 45.67 # Non-medical highest.

def three_max_money():
    money_list = []
    department_annual_salary = {}
    for a, b in zip(department, annual_salary):
        if b != '' and not ('medical' in a.lower()):
            now_money = float(b[1:])
            money_list.append(now_money)
            department_annual_salary[b] = a
    money_list.sort(reverse=True)
    print('highesthourlywage')
    print('highest =', end='')
    print(department_annual_salary.get('$' + str(money_list[0]) + '0'), '&' + str(money_list[0]) + '0')
    print('second = ', end='')
    print(department_annual_salary.get('$' + str(money_list[1]) + '0'), '&' + str(money_list[1]) + '0')
    print('third = ', end='')
    print(department_annual_salary.get('$' + str(money_list[2]) + '0'), '&' + str(money_list[2]) + '0')
    print()
