number_of_heroes = int(input())
chosen_heroes = {}

for hero in range(number_of_heroes):
    hero_stats = input().split()

    hero_name = hero_stats[0]
    hero_points = int(hero_stats[1])
    hero_mana = int(hero_stats[2])

    chosen_heroes[hero_name] = {'HP': hero_points, 'MP': hero_mana}

command = input()

while command != 'End':
    command = command.split(' - ')
    current_command = command[0]

    if current_command == 'CastSpell':
        hero_name = command[1]
        current_needed_mp = int(command[2])
        spell_name = command[3]

        if chosen_heroes[hero_name]['MP'] >= current_needed_mp:
            chosen_heroes[hero_name]['MP'] -= current_needed_mp
            print(f"{hero_name} has successfully cast {spell_name} and now has {chosen_heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif current_command == 'TakeDamage':
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        chosen_heroes[hero_name]['HP'] -= damage
        if chosen_heroes[hero_name]['HP'] > 0:
            print(
                f"{hero_name} was hit for {damage} HP by {attacker} and now has {chosen_heroes[hero_name]['HP']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del chosen_heroes[hero_name]
    elif current_command == 'Recharge':
        hero_name = command[1]
        amount = int(command[2])
        mp_before_recharge = chosen_heroes[hero_name]['MP']
        chosen_heroes[hero_name]['MP'] += amount
        if chosen_heroes[hero_name]['MP'] > 200:
            chosen_heroes[hero_name]['MP'] = 200
        recharged_mp = chosen_heroes[hero_name]['MP'] - mp_before_recharge
        print(f"{hero_name} recharged for {recharged_mp} MP!")
    elif current_command == 'Heal':
        hero_name = command[1]
        amount = int(command[2])
        hp_before_recharge = chosen_heroes[hero_name]['HP']
        chosen_heroes[hero_name]['HP'] += amount
        if chosen_heroes[hero_name]['HP'] > 100:
            chosen_heroes[hero_name]['HP'] = 100
        recharged_hp = chosen_heroes[hero_name]['HP'] - hp_before_recharge
        print(f"{hero_name} healed for {recharged_hp} HP!")

    command = input()

for name, value in chosen_heroes.items():
    print(name)
    hp = value['HP']
    mp = value['MP']
    print(f" HP: {hp}")
    print(f" MP: {mp}")
