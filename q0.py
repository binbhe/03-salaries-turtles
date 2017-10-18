#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

solution = "DIMAGGIO" # LAST NAME IN CAPS.

def job():
    first = 0
    for job, annual_salary_money in zip(job_title, annual_salary):
        if annual_salary_money != '':
            money = float(annual_salary_money[1:])
            if money > first:
                first = money

    for job, annual_salary_money in zip(job_title, annual_salary):
        if annual_salary_money != '' and annual_salary_money == ('$' + str(first) + '0'):
            print('MostSalaries')
            print(job.strip('/"').strip(), annual_salary_money)
            print()
            break
