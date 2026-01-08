money_as_string = input().split(', ')
count_of_beggars = int(input())

money_as_integer = []
result = []

start_index = 0

for money in  money_as_string:
    money_as_integer.append(int(money))

for begger in range(count_of_beggars):
    current_sum = 0
    for index in range(start_index,len(money_as_integer),count_of_beggars):
        current_sum += money_as_integer[index]
    result.append(current_sum)
    start_index += 1

print(result)




