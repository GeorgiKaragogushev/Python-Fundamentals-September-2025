current_string = input()
command = input()

while command != 'Done':

    command = command.split()
    action = command[0]
    if action == 'TakeOdd':
        password = ''
        for index in range(len(current_string)):
            if index % 2 != 0:
                password += current_string[index]
        current_string = password
        print(current_string)
    elif action == 'Cut':
        index = int(command[1])
        lenght = int(command[2])
        before_current_index = current_string[:index]
        after_current_index = current_string[index + lenght:]
        current_string = before_current_index + after_current_index
        print(current_string)
    elif action == 'Substitute':
        substring = command[1]
        subtitute = command[2]
        if substring in current_string:
            current_string = current_string.replace(substring, subtitute)
            print(current_string)
        else:
            print('Nothing to replace!')
    command = input()

print(f"Your password is: {current_string}")
