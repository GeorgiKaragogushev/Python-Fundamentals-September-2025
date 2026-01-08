numbers = list(map(int,input().split(', ')))


even_index = [i for i in range(len(numbers)) if numbers[i] % 2 == 0]

print(even_index)
