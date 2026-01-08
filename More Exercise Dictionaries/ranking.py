contest_dict = {}
take_part_in_contest_dict = {}

input_lines = input()
while input_lines != "end of contests":
    contest,password  = input_lines.split(':')

    if contest not in contest_dict:
        contest_dict[contest] = password
    input_lines = input()

input_lines = input()
while input_lines != "end of submissions":
    contest,password,username,points  = input_lines.split('=>')
    points = int(points)

    if contest in contest_dict:
        if contest_dict[contest] == password:
            if username not in take_part_in_contest_dict:
                take_part_in_contest_dict[username] = {}
            if contest not in take_part_in_contest_dict[username] or \
                points > take_part_in_contest_dict[username][contest]:
                take_part_in_contest_dict[username][contest] = points

    input_lines = input()
best_points = 0
user_most_points = ''
for name,value in take_part_in_contest_dict.items():
    total_points = sum(value.values())
    if total_points > best_points:
        best_points = total_points
        user_most_points = name

print(f"Best candidate is {user_most_points} with total {best_points} points.")
print('Ranking:')

for name,value in sorted(take_part_in_contest_dict.items()):
    print(name)
    for contest,points in sorted(value.items(), key=lambda x: x[1], reverse = True):
        print(f'#  {contest} -> {points}')
