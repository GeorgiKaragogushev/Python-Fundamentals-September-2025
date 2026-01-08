from math import ceil
def calculating_hours (first,second,third,people_count):
    total_people_per_hour = first + second + third
    total_hours = ceil(people_count / total_people_per_hour)
    return total_hours



first_man = int(input())
second_man = int(input())
third_man = int(input())
students_count = int(input())
print(calculating_hours(first_man,second_man,third_man,students_count))

