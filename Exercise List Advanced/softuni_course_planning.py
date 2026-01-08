current_course = input().split(', ')
command = input()
while command != 'course start':
    command = command.split(':')
    action = command[0]

    if action == 'Add':
        lesson_name = command[1]
        if lesson_name not in current_course:
            current_course.append(lesson_name)
    elif action == 'Insert':
        lesson_name = command[1]
        index = int(command[2])
        if lesson_name not in current_course:
            current_course.insert(index,lesson_name)
    elif action == 'Remove':
        lesson_name = command[1]
        if lesson_name in current_course:
            current_course.remove(lesson_name)
    elif action == 'Swap':
        first_lesson_name = command[1]
        second_lesson_name = command[2]
        if first_lesson_name and second_lesson_name in current_course:
            first_lesson_index = current_course.index(first_lesson_name)
            second_lesson_index = current_course.index(second_lesson_name)
            if f'{first_lesson_name}-Exercise' in current_course:
                current_course[first_lesson_index],current_course[second_lesson_index] = current_course[second_lesson_index],current_course[first_lesson_index]
                first_lesson_index_after_swap = current_course.index(first_lesson_name)
                current_course.remove(f'{first_lesson_name}-Exercise')
                current_course.insert(first_lesson_index_after_swap+1,f'{first_lesson_name}-Exercise')
            elif f'{second_lesson_name}-Exercise' in current_course:
                current_course[first_lesson_index], current_course[second_lesson_index] = current_course[second_lesson_index], current_course[first_lesson_index]
                second_lesson_index_after_swap = current_course.index(second_lesson_name)
                current_course.remove(f'{second_lesson_name}-Exercise')
                current_course.insert(second_lesson_index_after_swap+1, f'{second_lesson_name}-Exercise')
            elif  f'{first_lesson_name}-Exercise' and f'{second_lesson_name}-Exercise' in current_course:
                current_course[first_lesson_index],current_course[first_lesson_index+1],\
                current_course[second_lesson_index],current_course[second_lesson_index+1] = \
                current_course[second_lesson_index], current_course[second_lesson_index + 1], \
                current_course[first_lesson_index], current_course[first_lesson_index + 1]
            else:
                current_course[first_lesson_index],current_course[second_lesson_index] = current_course[second_lesson_index],current_course[first_lesson_index]

    elif action == 'Exercise':
        lesson_name = command[1]
        if lesson_name in current_course:
            if f'{lesson_name}-Exercise' not in current_course:
                lesson_index = current_course.index(lesson_name)
                current_course.insert(lesson_index+1,f'{lesson_name}-Exercise')
        else:
            current_course.append(lesson_name)
            current_course.append(f'{lesson_name}-Exercise')
    command = input()

for i in range(0,len(current_course)):
    ordered = i +1
    print(f'{ordered}.{current_course[i]}')