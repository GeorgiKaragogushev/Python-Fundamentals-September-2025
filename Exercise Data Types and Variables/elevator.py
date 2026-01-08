people_numbers = int(input())
capacy = int(input())


total_courses = people_numbers // capacy

left_people = people_numbers % capacy

if left_people > 0:
    total_courses += 1


print(total_courses)
