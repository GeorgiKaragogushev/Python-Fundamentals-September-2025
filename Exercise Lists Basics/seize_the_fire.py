fire_level = input().split("#")
amount_of_water = int(input())
effort = 0
total_fire = 0

print('Cells:')

for value in fire_level:
    first_fire_value = value.split(' = ')
    fire_type, fire_value = first_fire_value[0], int(first_fire_value[1])


    if amount_of_water < fire_value:
        continue
    elif amount_of_water <= 0:
        break


    if fire_type == 'Low':
        if 1 <= fire_value <= 50:
            amount_of_water -= fire_value
            effort += fire_value * 0.25
        else:
            continue

    elif fire_type == "Medium":
        if 51 <= fire_value <= 80:
            amount_of_water -= fire_value
            effort += fire_value * 0.25
        else:
            continue

    elif fire_type == "High":
        if 81 <= fire_value <= 125:
            amount_of_water -= fire_value
            effort += fire_value * 0.25
        else:
            continue

    total_fire += fire_value


    print(f"- {fire_value}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")




