password = input()
new_password = ''
command = input()
freezed = 0
is_freezed = False
while new_password != password and command != 'Error':
    current_command = command.split()
    action = current_command[0]

    if is_freezed:
        freezed += 1
        if freezed >= 2:
            is_freezed = False
            freezed = 0
        command = input()
        continue

    if action == 'Infuse':
        characters = current_command[1]
        new_password += characters
        print(new_password)
    elif action == 'Transpose':
        first_index = int(current_command[1])
        second_index = int(current_command[2])
        if first_index < 0 or second_index >= len(new_password):
            print('Failed attempt to unlock the treasure')
            command = input()
            continue
        if first_index > second_index:
            first_index,second_index = second_index,first_index
        new_password = new_password[:first_index] + new_password[second_index] + new_password[first_index + 1:second_index] + new_password[first_index] + new_password[second_index + 1:]
        print(new_password)
    elif action == 'Retrace':
        index = int(current_command[1])
        reversed_string = new_password[:index + 1][::-1]
        new_password = reversed_string + new_password[index + 1:]
        print(new_password)

    elif action == 'Destroy':
        character = current_command[1]
        if character in new_password:
            new_password = new_password.replace(character, '')
            print(new_password)
        else:
            print(f'Character {character} is invalid')
    elif action == 'Freeze':
        is_freezed = True
    command = input()
if new_password == password:
    print("The Golden Treasure has been unlocked!")
else:
    print(f"The string {new_password} does not match the password {password}!")

