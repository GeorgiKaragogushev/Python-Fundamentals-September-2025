command = input()
student_list = {}
graduated = {}
while command != 'Summer':
    action,info = command.split(': ')
    info = info.split('#')
    if action == 'Register':
        student_id = info[0]
        student_name = info[1]
        field_of_duty = info[2]
        if student_id not in student_list:
            student_list[student_id] = {'name':student_name,'duty':field_of_duty}
        else:
            print(f"RegistrationError: Student with ID {student_id} is already in the system!" )
    elif action == 'Change Field':
        student_id = info[0]
        new_field_of_duty = info[1]
        if student_id not in student_list:
            print(f'StudentNotFoundError: Student with ID {student_id} does not exist in the system!')
        else:
            student_list[student_id]['duty'] = new_field_of_duty
    elif action == 'Graduate':
        field_of_duty = info[0]
        for student in student_list:
            if student_list[student]['duty'] == field_of_duty:
                student_name = student_list[student]['name']
                student_duty = student_list[student]['duty']
                graduated[student] = {'name':student_name,'duty':student_duty}

    command = input()

for student in graduated:
    del student_list[student]


if student_list:
    print('All Students:')
    for student,student_info in student_list.items():
        student_name = student_info['name']
        student_duty = student_info['duty']
        print(f'*ID {student} -> {student_name} studies {student_duty}')
else:
    print("There are no students at the university system")

if graduated:
    print('All Graduates:')
    for student,student_info in graduated.items():
        student_name = student_info['name']
        student_duty = student_info['duty']
        print(f"*{student_name} graduated university with {student_duty}")
else:
    print("There are no university graduates")