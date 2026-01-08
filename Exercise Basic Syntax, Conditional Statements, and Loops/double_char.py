while True:
    command = input()

    if command == 'End':
        break
    elif command == 'SoftUni':
        continue

    doubled_word = ''

    for letter in command:
        doubled_word += letter * 2
    print(doubled_word)

