users_dict = {}
number_of_lines = int(input())

for _ in range(number_of_lines):
    user_info = input().split()
    command = user_info[0]

    if command == 'register':
        user,license_number = user_info[1],user_info[2]
        if user in users_dict:
            print(f"ERROR: already registered with plate number {license_number}")
        else:
            users_dict[user] = license_number
            print(f"{user} registered {license_number} successfully")

    elif command == 'unregister':
        user = user_info[1]
        if user not in users_dict:
            print(f"ERROR: user {user} not found")
        else:
            del users_dict[user]
            print(f"{user} unregistered successfully")

for user,license_number in users_dict.items():
    print(f"{user} => {license_number}")

