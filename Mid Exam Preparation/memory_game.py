sequence_of_elements = input().split()
moves = 0

while sequence_of_elements:
    command = input()
    if command == 'end':
        break
    moves += 1
    indexes = command.split()
    first_index, second_index = int(indexes[0]), int(indexes[1])

    if (first_index == second_index or
            first_index not in range(len(sequence_of_elements)) or
            second_index not in range(len(sequence_of_elements))):

        middle = len(sequence_of_elements) // 2
        sequence_of_elements = sequence_of_elements[:middle] + ([f"-{moves}a"] * 2) + sequence_of_elements[middle:]
        print("Invalid input! Adding additional elements to the board")
        continue

    if sequence_of_elements[first_index] == sequence_of_elements[second_index]:
        print(f"Congrats! You have found matching elements - {sequence_of_elements[first_index]}!")
        higher_index = max(first_index, second_index)
        lower_index = min(first_index, second_index)
        del sequence_of_elements[higher_index]
        del sequence_of_elements[lower_index]
    else:
        print('Try again!')

if not sequence_of_elements:
    print(f"You have won in {moves} turns!")
else:
    print(f"Sorry you lose :(\n{' '.join(sequence_of_elements)}")
