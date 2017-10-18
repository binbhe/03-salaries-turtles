#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

solution = 67.89 # Highest hourly as a float.

def hourly_rate_money():
    max_money = 0
    for money in hourly_rate:
        if money != '':
            money = float(money[1:])
            if max_money < money:
                max_money = money
    print('highesthourlywage')
    print(max_money)
    print()
