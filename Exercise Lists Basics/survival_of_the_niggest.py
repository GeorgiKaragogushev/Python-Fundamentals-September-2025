numbers = input().split()
count_to_remove = int(input())

min_number = 0
flipped_to_int = []
result = []

for element in numbers:
    integer_number = int(element)
    flipped_to_int.append(integer_number)


for i in range(count_to_remove):
    min_number = min(flipped_to_int)
    flipped_to_int.remove(min_number)

for number in flipped_to_int:
    result.append(str(number))

print(', '.join(result))





