sequence_of_numbers = input().split()
string = input()

result = []
string_list = []

for element in string:
    string_list.append(element)


for number in sequence_of_numbers:
    index = 0
    for digit in number:
        index += int(digit)




    if index >= len(string_list):
        new_index = index % len(string_list)
        popped_char = string_list.pop(new_index)
        result.append(popped_char)
    else:
        popped_char = string_list.pop(index)
        result.append(popped_char)

print("".join(result))

