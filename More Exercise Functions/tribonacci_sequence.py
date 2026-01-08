def tribunacci_number (n):
    numbers_list = [1]
    for i in range(1,n):
        if i == 1:
            numbers_list.append(num)
        elif i == 2:
            numbers_list.append(num)
        else:
            next_num = numbers_list[-1] + numbers_list[-2] + numbers_list[-3]
            numbers_list.append(next_num)
    return numbers_list

number = int(input())

result = tribunacci_number(number)

number_as_string = []

for num in result:
    number_as_string.append(str(num))

print(' '.join(number_as_string))
