house_name = ''

while True:
    name = input()

    if name == 'Welcome!':
        print("Welcome to Hogwarts.")
        break
    elif name == 'Voldemort':
        print("You must not speak of that name!")
        break

    if len(name) < 5:
        house_name = 'Gryffindor'
    elif len(name) == 5:
        house_name = 'Slytherin'
    elif len(name) == 6:
        house_name = 'Ravenclaw'
    elif len(name) > 6:
        house_name = 'Hufflepuff'

    print(f"{name} goes to {house_name}.")
