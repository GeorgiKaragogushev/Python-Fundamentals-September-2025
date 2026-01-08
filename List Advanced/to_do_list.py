my_list_as_string = ['0'] * 10

while True:

    notes = input().split('-')

    if notes[0] == 'End':
        result = [element for element in my_list_as_string if element != '0']
        print(result)
        break

    index = int(notes[0]) - 1

    my_list_as_string.pop(index)
    my_list_as_string.insert(index, notes[1])





