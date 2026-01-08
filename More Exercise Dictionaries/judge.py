command = input()

contest_info = {}
individual_stats = {}

while command != 'no more time':
    username,contest,points = command.split(' -> ')

    if contest not in contest_info:
        contest_info[contest] = {}
    if username not in contest_info[contest]:
        contest_info[contest][username] = int(points)

    elif username in contest_info[contest]:
        if int(contest_info[contest][username]) < int(points):
            contest_info[contest][username] = int(points)
    command = input()

for current_contest,info in contest_info.items():
    print(f'{current_contest}: {len(info)} participants')
    number = 1
    for name,points in sorted(info.items(),key=lambda x: (-x[1],x[0])):
        print(f'{number}. {name} <::> {points}')
        number +=1

        if name not in individual_stats:
            individual_stats[name] = 0
        individual_stats[name] += int(points)

print('Individual standings:')
number = 1
for user,points in sorted(individual_stats.items(), key=lambda x: (-x[1], x[0])):
    print(f'{number}. {user} -> {points}')
    number+=1