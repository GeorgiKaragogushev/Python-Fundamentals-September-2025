start_energy = 100
start_coins = 100
is_open = True

events = input().split('|')

for event in events:
    event_values = event.split('-')
    event_type, event_number = event_values[0],int(event_values[1])


    if event_type == 'rest':
        current_energy = start_energy
        start_energy += event_number
        if  start_energy > 100:
            start_energy = 100
        gained_energy = start_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {start_energy}.")
    elif event_type == 'order':

        if start_energy >= 30:
            start_energy -= 30
            start_coins += event_number
            print(f"You earned {event_number} coins.")
        else:
            start_energy += 50
            print('You had to rest!')
            continue
    else:
        if start_coins >= event_number:
            start_coins -= event_number
            print(f'You bought {event_type}.')
        else:
            is_open = False
            print(f'Closed! Cannot afford {event_type}.')
            break

if is_open:
    print('Day completed!')
    print(f'Coins: {start_coins}')
    print(f'Energy: {start_energy}')







