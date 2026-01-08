number = float(input())

if number == 0:
    print("zero")

elif 1<= number <= 1000000:
    print("positive")

elif 0 <number < 1:
    print("small positive")

elif number > 1000000:
    print("large positive")

elif -1 < number < 1:
    print("small negative")

elif number < -1000000:
    print("large negative")

else:
    print("negative")

