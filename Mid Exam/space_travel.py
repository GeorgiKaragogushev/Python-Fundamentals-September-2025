def travel(current_fuel,current_value):
        if current_fuel >= current_value:
            current_fuel -= current_value
            return f"The spaceship travelled {current_value} light-years.",current_fuel
        return 'Mission failed.',current_fuel

def enemy(current_fuel,current_amunitions,current_armour):
        if current_amunitions >= current_armour:
            current_amunitions -= current_armour
            return f"An enemy with {current_armour} armour is defeated.",current_fuel,current_amunitions
        elif current_fuel >= current_armour * 2:
            current_fuel -= current_armour * 2
            return f"An enemy with {current_armour} armour is outmaneuvered.",current_fuel,current_amunitions
        return "Mission failed.",current_fuel,current_amunitions


def repair(current_fuel,current_amunitions,current_value):
    current_fuel += current_value
    current_amunitions += current_value * 2
    return f"Ammunitions added: {current_value * 2}.\nFuel added: {current_value}.",current_fuel,current_amunitions


def titan():
    return "You have reached Titan, all passengers are safe."


travel_route_to_titan = input().split("||")
fuel_amount = int(input())
ammunition_amount = int(input())

for route in travel_route_to_titan:
    command = route.split()

    if route == 'Titan':
        print('You have reached Titan, all passengers are safe.')
        break
    else:
        command, value = route.split()
        value = int(value)

    if command == 'Travel':
        message,fuel_amount = travel(fuel_amount,value)
        print(message)
        if message == 'Mission failed.':
            break

    elif command == 'Enemy':
       message,fuel_amount,ammunition_amount = enemy(fuel_amount,ammunition_amount,value)
       print(message)
       if message == 'Mission failed.':
           break

    elif command == 'Repair':
        message,fuel_amount,ammunition_amount = repair(fuel_amount,ammunition_amount,value)
        print(message)
        if message == 'Mission failed.':
            break
