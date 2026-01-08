travel_route_to_titan = input().split("||")
fuel_amount = int(input())
ammunition_amount = int(input())

for route in travel_route_to_titan:

    if route == 'Titan':
        print('You have reached Titan, all passengers are safe.')
        break
    else:
        command,value = route.split()
        value = int(value)

    if command == 'Travel':
        if fuel_amount >= value:
            fuel_amount -= value
            print(f"The spaceship travelled {value} light-years.")
        else:
            print('Mission failed.')
            break

    elif command == 'Enemy':
        if ammunition_amount >= value:
            ammunition_amount -= value
            print(f"An enemy with {value} armour is defeated.")
        elif ammunition_amount < value and fuel_amount >= value * 2:
            fuel_amount -= value * 2
            print(f"An enemy with {value} armour is outmaneuvered.")
        else:
            print('Mission failed.')
            break

    elif command == 'Repair':
        fuel_amount += value
        ammunition_amount += value * 2
        print(f"Ammunitions added: {value * 2}.\nFuel added: {value}.")