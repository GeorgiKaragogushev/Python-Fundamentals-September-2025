import sys

num1 = int(input())
num2 = int(input())
num3 = int(input())

max_number = -sys.maxsize


if num1 > num2 and num1 > num3:
    max_number = num1
elif num2 > num1 and  num2 > num3:
    max_number = num2
else:
    max_number = num3

print(max_number)

# another solving method

num1 = int(input())
num2 = int(input())
num3 = int(input())

print(max(num1,num2,num3))