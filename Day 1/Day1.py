from typing import List  


def import_data(filename):
    with open(filename, 'r') as file:
        list1, list2 = [], []
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)
    return list1, list2
filename = '/Users/torsten/Desktop/AoC-2024/Day 1/input.txt'
list1, list2 = import_data(filename) 


def calculate_distance(list1, list2): 

    sorted_list1 = sorted(list1)
    sorted_list2 = sorted(list2)
    total_distance = 0

    for num1, num2 in zip(sorted_list1, sorted_list2):
        total_distance += abs(num1 - num2)

    return total_distance

print(calculate_distance(list1, list2))  




