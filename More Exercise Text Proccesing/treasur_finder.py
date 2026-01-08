keys = list(map(int, input().split()))
text = input()


while text != 'find':
    start_index = 0
    end_index = 0
    coordinates = ''
    index = 0

    for i in range(len(text)):
        if i >= len(text):
            break
        if index >= len(keys):
            index = 0
        coordinates += chr(ord(text[i]) - keys[index])
        index += 1

    for index in range(len(coordinates)):
        if coordinates[index] == '&':
            if not start_index:
                start_index = index
            else:
                end_index = index
    material = coordinates[start_index + 1:end_index]

    for index in range(len(coordinates)):
        if coordinates[index] == '<':
            start_index = index
        elif coordinates[index] == '>':
            end_index = index
    coords = coordinates[start_index + 1:end_index]

    text = input()

    print(f'Found {material} at {coords}')







ч







