number_lines = int(input())
capacy_litters = 255
total_liters = 0

for line in range(number_lines):
    litters = int(input())


    if total_liters+litters > capacy_litters:
        print("Insufficient capacity!")
    else:
        total_liters += litters

print(total_liters)


