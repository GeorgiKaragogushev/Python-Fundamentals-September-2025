import re

racers = input().split(', ')
pattern = r'[A-Za-z]+'

racers_info = {}

command = input()

while command != "end of race":
    racer_name = ''.join(re.findall(pattern, command))
    if racer_name in racers:
        if racer_name not in racers_info:
            racers_info[racer_name] = 0
        for digit in command:
            if digit.isdigit():
                racers_info[racer_name] += int(digit)

    command = input()
iteration_order = 1
for name, value in sorted(racers_info.items(), key=lambda x: x[1], reverse=True)[:3]:

    if iteration_order == 1:
        print(f'1st place: {name}')
    elif iteration_order == 2:
        print(f'2nd place: {name}')
    else:
        print(f'3rd place: {name}')
    iteration_order += 1
