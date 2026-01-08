storage = {}

command = input()
while command != 'Lumpawaroo':
    if ' | ' in command:
        command = command.split(' | ')
        is_found = False

        force_side = command[0]
        force_user = command[1]

        if force_side not in storage:
            storage[force_side] = []
        for side, info in storage.items():
            if force_user in info:
                is_found = True
                break
        if not is_found:
            storage[force_side].append(force_user)


    elif ' -> ' in command:
        command = command.split(' -> ')
        force_user = command[0]
        force_side = command[1]
        for side in storage.keys():
            if force_user in storage[side]:
                storage[side].remove(force_user)

        if force_side not in storage:
            storage[force_side] = []
        storage[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

    command = input()

for side, info in storage.items():
    if len(info):
        print(f'Side: {side}, Members: {len(info)}')
        for name in info:
            print(f'! {name}')
