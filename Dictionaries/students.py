students_dict = {}


while True:
    command = input()

    if ":" not in command:
        command = command.replace('_',' ')
        for student, info in students_dict.items():
            if info['course'] == command:
                print(f"{student} - {info['ID']}")
        break

    name, student_id, course = command.split(':')

    students_dict[name] = {'ID': student_id, 'course': course}

