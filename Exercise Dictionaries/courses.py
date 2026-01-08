courses_dict = {}

command = input()
while command != 'end':
    course,student_name = command.split(' : ')
    if course not in courses_dict:
        courses_dict[course] = []
    if student_name not in courses_dict[course]:
        courses_dict[course].append(student_name)
    command = input()

for course,value in courses_dict.items():
    print(f'{course}: {len(value)}')
    for user in value:
        print(f'-- {user}')

