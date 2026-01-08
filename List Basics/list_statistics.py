number_of_lines = int(input())

first_list = []
second_list = []

for i in range(number_of_lines):
    number = int(input())

    if number >= 0:
        first_list.append(number)
    else:
        second_list.append(number)

print(first_list)
print(second_list)
print(f"Count of positives: {len(first_list)}")
print(f"Sum of negatives: {sum(second_list)}")


