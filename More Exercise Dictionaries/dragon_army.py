number_of_dragons = int(input())
dragon_stats = {}

for dragon in range(number_of_dragons):
    dragon_type,dragon_name,dragon_damage,dragon_health,dragon_armour = input().split()

    if dragon_damage == 'null':
        dragon_damage = 45
    if dragon_health == 'null':
        dragon_health = 250
    if dragon_armour == 'null':
        dragon_armour = 10

    if dragon_type not in dragon_stats:
        dragon_stats[dragon_type] = {}
    if dragon_name not in dragon_stats[dragon_type]:
        dragon_stats[dragon_type][dragon_name] = [dragon_damage,dragon_health,dragon_armour]
    elif dragon_name in dragon_stats[dragon_type]:
        dragon_stats[dragon_type][dragon_name] = [dragon_damage,dragon_health,dragon_armour]

for dragon_type,info in dragon_stats.items():
    average_damage = 0
    average_health = 0
    average_armour = 0
    for name,values in info.items():
        average_damage += int(values[0])
        average_health += int(values[1])
        average_armour += int(values[2])

    average_damage/= len(info)
    average_health/= len(info)
    average_armour/= len(info)

    print(f'{dragon_type}::({average_damage:.2f}/{average_health:.2f}/{average_armour:.2f})')
    for name, values in sorted(info.items()):
        print(f'-{name} -> damage: {values[0]}, health: {values[1]}, armor: {values[2]}')






