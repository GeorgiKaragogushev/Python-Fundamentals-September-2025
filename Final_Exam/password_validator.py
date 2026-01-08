password = input()
command = input()
while command != 'Complete':
    current_command = command.rsplit(' ', 1)
    action = current_command[0]
    if action == 'Make Upper':
        index = int(current_command[1])
        if -1 < index < len(password):
            password = password.replace(password[index],password[index].upper())
            print(password)
    elif action == 'Make Lower':
        index = int(current_command[1])
        if -1 < index < len(password):
            password = password.replace(password[index],password[index].lower())
            print(password)
    else:
        current_command = command.split()
        action = current_command[0]
    if action == 'Insert':
        index = int(current_command[1])
        char = current_command[2]
        if -1 < index < len(password):
            password = password[:index] + char + password[index:]
            print(password)

    elif action == 'Replace':
        char = current_command[1]
        value = int(current_command[2])
        if char in password:
            new_char = chr(ord(char) + value)
            password = password.replace(char, new_char)
            print(password)
    elif action == 'Validation':
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        lower_case = 0
        upper_case = 0
        for char in password:
            if not (char.isalnum() or char == '_'):
                print("Password must consist only of letters, digits and _!")
        for char in password:
            if char.isupper():
                upper_case += 1
            elif char.islower():
                lower_case += 1

        if upper_case == 0:
            print("Password must consist at least one uppercase letter!")

        if lower_case == 0:
            print("Password must consist at least one lowercase letter!")

        digits_count = 0
        for char in password:
            if char.isdigit():
                digits_count += 1
        if digits_count == 0:
            print("Password must consist at least one digit!")
    command = input()


