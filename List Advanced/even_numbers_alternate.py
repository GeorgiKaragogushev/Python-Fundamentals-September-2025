numbers = list(map(int,input().split(', ')))

even_index = map(lambda i: i if numbers[i] % 2 == 0 else 'no',range(len(numbers)))

filterred_index = list(filter(lambda x: x != 'no', even_index))

print(filterred_index)

