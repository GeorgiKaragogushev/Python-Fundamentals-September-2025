lines = int(input())

for line in range(lines):
    text = input()

    name = ''
    age = ''

    start_index = text.index('@')
    end_index = text.index('|')

    for index in range(start_index + 1, end_index):
        name += text[index]

    start_index = text.index('#')
    end_index = text.index('*')

    for index in range(start_index + 1, end_index):
        age += text[index]

    print(f'{name} is {age} years old.')
