number = int(input())

for num in range(1,number+1):
    print(num *'*')

    if num == number:
        for num2 in range(number-1,0,-1):
            print(num2 * '*')