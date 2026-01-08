numbers = input().split()
k_number = int(input())
index = 0
my_list = []
while numbers:
    index = (index + k_number -1) % len(numbers)
    my_list.append(numbers.pop(index))

print(f"[{','.join(my_list)}]")