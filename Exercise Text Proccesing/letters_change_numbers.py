string_input = input().split()
total_sum = 0

for word in string_input:
    first_letter = word[0]
    last_letter = word[-1]
    numbers_in_middle = int(word[1:-1])

    if first_letter.isupper():
        total_sum += numbers_in_middle / (ord(first_letter) - 64)
    elif first_letter.islower():
        total_sum += numbers_in_middle * (ord(first_letter) - 96)

    if last_letter.isupper():
        total_sum -= (ord(last_letter) - 64)
    elif last_letter.islower():
        total_sum += (ord(last_letter) - 96)

print(f'{total_sum:.2f}')