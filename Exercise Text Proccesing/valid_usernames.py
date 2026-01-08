def name_lenght(username: str) -> bool:
    if 3 <= len(username) <= 16:
        return True
    return False


def allowed_symbols(username: str) -> bool:
    for char in username:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    return True


def find_result(username: str) -> bool:
    if name_lenght(username) and allowed_symbols(username):
        valid_name = True
        return valid_name
    return False


names = input().split(', ')
valid_name = False

for name in names:
    valid_name = find_result(name)
    if valid_name:
        print(name)
