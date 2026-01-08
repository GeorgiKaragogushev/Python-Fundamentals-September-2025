numbers = input().split(', ')

zero_count = numbers.count('0')
int_number_list = []

while "0" in numbers:
    numbers.remove('0')
for index in range(zero_count):
    numbers.append('0')

for number in numbers:
    int_number = int(number)
    int_number_list.append(int_number)
print(int_number_list)