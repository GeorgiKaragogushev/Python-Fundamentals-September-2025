def is_palindrome(some_numbers: str):
    return some_numbers == some_numbers[::-1]

numbers = input().split(", ")

for number in numbers:
    print(is_palindrome(number))


