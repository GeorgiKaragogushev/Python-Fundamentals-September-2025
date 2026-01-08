first_string = input()
second_string = input()
new_string = ''

for index in range(len(second_string)):
    if first_string[index]!= second_string[index]:
        temp_string = second_string[:index + 1] + first_string[index + 1:]
        new_string = temp_string
        print(new_string)


