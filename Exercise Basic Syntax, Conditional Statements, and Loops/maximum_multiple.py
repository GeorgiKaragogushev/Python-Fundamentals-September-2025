import sys

devisor = int(input())
boundary = int(input())
max_num = -sys.maxsize


for num in range(boundary + 1):
    if num % devisor == 0:
        if max_num < num:
            max_num = num

print(max_num)