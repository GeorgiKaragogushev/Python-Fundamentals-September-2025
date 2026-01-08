string = input().split()
my_list = []

for number in string:
    new_number = -int(number)
    my_list.append(new_number)

print(my_list)
