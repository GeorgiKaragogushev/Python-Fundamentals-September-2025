def max_num():
    return max(integers)


def min_num():
    return min(integers)


def sum_num():
    return sum(integers)


def result():
    print(f"The minimum number is {min_num()}")
    print(f"The maximum number is {max_num()}")
    print(f"The sum number is: {sum_num()}")


numbers = input().split()
integers = []

for num in numbers:
    integers.append(int(num))

result()
