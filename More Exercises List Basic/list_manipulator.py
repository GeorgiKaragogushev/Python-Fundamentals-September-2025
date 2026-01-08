def exchange(current_numbers, current_command):
    index = int(current_command[1])
    if index < 0 or index >= len(current_numbers):
        print('Invalid index')
        return current_numbers
    first_half = current_numbers[:index + 1]
    second_half = current_numbers[index + 1:]
    current_numbers = second_half + first_half
    return current_numbers


def max_func(current_numbers, current_command):
    max_num = ''
    if current_command[1] == 'even':
        even_numbers = [num for num in current_numbers if num % 2 == 0]
        if even_numbers:
            max_num = max(even_numbers)
        else:
            print('No matches')
            return current_numbers
    elif current_command[1] == 'odd':
        odd_numbers = [num for num in current_numbers if num % 2 != 0]
        if odd_numbers:
            max_num = max(odd_numbers)
        else:
            print('No matches')
            return current_numbers

    for i in range(len(current_numbers) - 1, -1, -1):
        if current_numbers[i] == max_num:
            print(i)
            break

    return current_numbers


def min_func(current_numbers, current_command):
    min_num = ''
    if current_command[1] == 'even':
        even_numbers = [num for num in current_numbers if num % 2 == 0]
        if even_numbers:
            min_num = min(even_numbers)
        else:
            print('No matches')
            return current_numbers
    elif current_command[1] == 'odd':
        odd_numbers = [num for num in current_numbers if num % 2 != 0]
        if odd_numbers:
            min_num = min(odd_numbers)
        else:
            print('No matches')
            return current_numbers
    for i in range(len(current_numbers) - 1, -1, -1):
        if current_numbers[i] == min_num:
            print(i)
            break
    return current_numbers


def first(current_numbers, current_command):
    count = int(current_command[1])
    if count > len(current_numbers):
        print("Invalid count")
        return current_numbers
    first_even = []
    first_odd = []
    if current_command[2] == 'even':
        for num in current_numbers:
            if num % 2 == 0:
                first_even.append(num)
                if len(first_even) == count:
                    break
        print(first_even)

    elif current_command[2] == 'odd':
        for num in current_numbers:
            if num % 2 != 0:
                first_odd.append(num)
                if len(first_odd) == count:
                    break
        print(first_odd)
    return current_numbers


def last(current_numbers, current_command):
    count = int(current_command[1])
    if count > len(current_numbers):
        print("Invalid count")
        return current_numbers
    last_two_even = []
    last_two_odd = []
    if current_command[2] == 'even':
        for num in current_numbers[::-1]:
            if num % 2 == 0:
                last_two_even.append(num)
                if len(last_two_even) == count:
                    break
        print(last_two_even[::-1])

    elif current_command[2] == 'odd':
        for num in current_numbers[::-1]:
            if num % 2 != 0:
                last_two_odd.append(num)
                if len(last_two_odd) == count:
                    break
        print(last_two_odd[::-1])
    return current_numbers

numbers = list(map(int, input().split()))
command = input()
while command != 'end':
    command = command.split()
    action = command[0]

    if action == 'exchange':
        numbers = exchange(numbers, command)
    elif action == 'max':
        numbers = max_func(numbers, command)
    elif action == 'min':
        numbers = min_func(numbers, command)
    elif action == 'first':
        numbers = first(numbers, command)
    elif action == 'last':
        numbers = last(numbers, command)

    command = input()

print(numbers)