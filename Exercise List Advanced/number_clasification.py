def positive(list_nums):
    return [num for num in list_nums if int(num) > -1]


def negative(list_nums):
    return [num for num in list_nums if int(num) < 0]


def even(list_nums):
    return [num for num in list_nums if int(num) % 2 == 0]


def odd(list_nums):
    return [num for num in list_nums if int(num) % 2 != 0]



numbers = input().split(', ')



print(f"Positive: {', '.join(positive(numbers))}")
print(f"Negative: {', '.join(negative(numbers))}")
print(f"Even: {', '.join(even(numbers))}")
print(f"Odd: {', '.join(odd(numbers))}")
