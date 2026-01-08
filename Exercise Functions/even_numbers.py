def even_num(n):
    return n % 2 == 0


numbers = input().split()
integers = []

for num in numbers:
    int_num = int(num)
    integers.append(int_num)

result = list(filter(even_num, integers))


print(result)
