text = input()

numbers_list = []
non_numbers_list = []

for element in text:
    if element.isdigit():
        numbers_list.append(element)
    else:
        non_numbers_list.append(element)

take_list = []
skip_list = []

for index in range(len(numbers_list)):
    if index % 2 == 0:
        take_list.append(numbers_list[index])
    else:
        skip_list.append(numbers_list[index])

result_string = ''

for number in zip(take_list,skip_list):
    for i in range(len(number)):
        if i % 2 == 0:
            take_lenght = int(number[i])
            if take_lenght == 0:
                continue
            result_string += ''.join(non_numbers_list[:take_lenght])
            del non_numbers_list[:take_lenght]
        else:
            skip_lenght = int(number[i])
            del non_numbers_list[:skip_lenght]

print(result_string)


