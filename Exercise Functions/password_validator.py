def chars_long(symbols):
    if 6 <= len(symbols) <= 10:
        return True
    return "Password must be between 6 and 10 characters"


def letters_digits(symbols):
    if symbols.isalnum():
        return True
    return "Password must consist only of letters and digits"


def digits_num(symbols):
    digits_count = 0
    for digit in symbols:
        if digit.isdigit():
            digits_count += 1
    if digits_count >= 2:
        return True
    return "Password must have at least 2 digits"

def is_valid(symbols):
    result = [chars_long(symbols), letters_digits(symbols), digits_num(symbols)]
    for element in range(len(result)-1,-1,-1):
        if isinstance(result[element],bool):
            result.pop(element)
    return result

password = input()
not_valid_password = (is_valid(password))

if not_valid_password:
    print('\n'.join(not_valid_password))
else:
    print('Password is valid')

