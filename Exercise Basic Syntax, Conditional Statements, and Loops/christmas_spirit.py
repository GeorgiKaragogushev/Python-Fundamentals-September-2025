quantity_of_decorations = int(input())
days_left_until_christmas = int(input())
christmas_spirit = 0
total_price = 0


for day in range(1,days_left_until_christmas+1):
    if day % 11 == 0:
        quantity_of_decorations += 2
    if day % 10 == 0:
        christmas_spirit -= 20
        total_price += 5 + 3 + 15

    if day % 2 == 0:
        total_price += quantity_of_decorations * 2
        christmas_spirit += 5
    if day % 3 == 0:
        if day % 5 == 0:
            christmas_spirit += 30
        christmas_spirit += 13
        total_price += (3+5) * quantity_of_decorations
    if day % 5 == 0:
        total_price += quantity_of_decorations * 15
        christmas_spirit += 17
if days_left_until_christmas % 10 == 0:
    christmas_spirit-=30

print(f'Total cost: {total_price}')
print(f'Total spirit: {christmas_spirit}')