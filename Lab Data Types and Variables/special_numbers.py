number = int(input())


for num in range(1,number+1):
    is_True = False
    total_score = 0


    for digit in str(num):
        digit = int(digit)


        total_score += digit

    if total_score == 5 or total_score == 7 or total_score == 11:
        is_True = True
        print(f"{num} -> {is_True}")

    else:
        print(f"{num} -> {is_True}")





