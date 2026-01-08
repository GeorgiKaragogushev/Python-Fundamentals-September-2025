students_info = {}
result_dict = {}
rows = int(input())

for _ in range(rows):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_info:
        students_info[student_name] = []
    students_info[student_name].append(student_grade)

for student,grades in students_info.items():
    avereage_grade = sum(grades) / len(grades)
    if avereage_grade >= 4.50:
        result_dict[student] = avereage_grade

for name,grade in result_dict.items():
    print(f'{name} -> {grade:.2f}')
