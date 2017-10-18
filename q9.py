#!/usr/bin/env python

from helper import get_data

vec = get_data("salaries.csv")

# Solution should contain the single
# police officer name with 37 occurrences.
solution = "JULIETTE"

def girl_name_police():
    count_name_set = set([])
    count_name_list = []
    for count_name, count_departement, count_full_part_time in zip(name, department, full_part_time):
        if 'detective' in count_departement.lower():
            count_name_list.append(count_name)
            count_name_set.add(count_name)

    for c_s in count_name_set:
        count = name.count(c_s)
        if count == 37:
            print('Womencommonname')
            print(c_s.strip('\"').strip())
            print()
            break
