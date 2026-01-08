def absolute_value (n):
   return abs(float(n))


my_list = []
numbers = input().split()

for num in numbers:
    int_num = float(num)
    result = absolute_value(int_num)
    my_list.append(result)

print(my_list)