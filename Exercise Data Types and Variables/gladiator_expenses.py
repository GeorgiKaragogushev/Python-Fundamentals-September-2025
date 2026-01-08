lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price =float(input())
armour_price = float(input())

broken_helmet_times = 0
broken_sword_times = 0
broken_shield_times = 0
broken_armour_times = 0

for fight in range(1,lost_fights+1):
    if fight % 2 == 0:
        broken_helmet_times += 1
    if fight % 3 == 0:
        broken_sword_times += 1
        if fight % 2 == 0:
            broken_shield_times += 1
            if broken_shield_times % 2 == 0 and broken_shield_times != 0:
                broken_armour_times +=1


total_sum = (broken_armour_times * armour_price) + (broken_helmet_times * helmet_price) + (broken_sword_times * sword_price) + (broken_shield_times * shield_price)

print(f'Gladiator expenses: {total_sum:.2f} aureus')