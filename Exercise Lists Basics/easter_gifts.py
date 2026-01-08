gifts = input().split()


while True:
    command = input()

    if command == 'No Money':
        while 'None' in gifts:
            gifts.remove('None')
        print(' '.join(gifts))
        break


    command_values = command.split()
    command_type, command_value = command_values[0],command_values[1]

    if command_type == 'OutOfStock':
        for value in gifts:
            if value == command_value:
                index_of_the_value = gifts.index(command_value)
                gifts[index_of_the_value] = 'None'


    elif command_type == "Required":
        if len(command_values) > 2:
            command_index = int(command_values[2])
            if -1 < command_index < len(gifts):
                gifts[command_index] = command_value


    elif command_type == 'JustInCase':
        gifts.pop()
        gifts.append(command_value)






