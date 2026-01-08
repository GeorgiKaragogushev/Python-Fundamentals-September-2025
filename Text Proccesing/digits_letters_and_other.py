string = input()

letters = ''
digits = ''
other_symbols = ''

for symbol in string:
    if symbol.isalpha():
        letters += symbol
    elif symbol.isdigit():
        digits += symbol
    else:
        other_symbols += symbol


print(digits)
print(letters)
print(other_symbols)