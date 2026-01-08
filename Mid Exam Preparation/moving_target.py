
def shoot_command (targets_list: list,target_index: int,target_power: int) -> list:
    if 0 <= target_index < len(targets_list):
        targets_list[target_index] -= target_power
        if targets_list[target_index] <= 0:
            targets_list.pop(target_index)
    return targets_list

def add_command (targets_list: list,target_index: int,target_power: int) -> list:
    if 0 <= target_index < len(targets_list):
        targets_list.insert(target_index,target_power)
    else:
        print("Invalid placement!")
    return targets_list

def strike_command (targets_list: list,target_index: int,target_power: int) -> list:
    start = target_index - target_power
    end = target_index + target_power
    if start < 0 or end >= len(targets_list):
        print("Strike missed!")
    else:
        targets_list =  targets_list[:start] + targets_list[end+1:]
    return targets_list
sequence_of_targets = list(map(int,input().split()))
while True:
    command = input()

    if command == 'End':
        print('|'.join([str(number) for number in sequence_of_targets]))
        break
    command = command.split()
    current_command = command[0]
    index = int(command[1])
    value = int(command[2])

    if current_command == 'Shoot':
        sequence_of_targets= shoot_command(sequence_of_targets,index,value)


    elif current_command == 'Add':
        sequence_of_targets = add_command(sequence_of_targets,index,value)

    elif current_command == 'Strike':
        sequence_of_targets = strike_command(sequence_of_targets, index, value)

