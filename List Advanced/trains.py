wagons = [0] * int(input())

while True:
    command = input().split()

    current_command = command[0]

    if current_command == 'End':
        print(wagons)
        break

    if current_command == 'add':
        people = int(command[1])
        wagons[-1] += people

    elif current_command == 'insert':
        wagons[int(command[1])] += int(command[2])

    elif current_command == 'leave':
        wagons[int(command[1])] -= int(command[2])




