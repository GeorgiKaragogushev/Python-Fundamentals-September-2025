
coffees_num = 0
total_coffees = 0

while True:
    command = input()

    if  command == 'End' or command == "END":
        if total_coffees > 5:
            print("You need extra sleep")
            break
        else:
            print(total_coffees)
            break
    elif command == 'coding':
        coffees_num = 1
        total_coffees += coffees_num
    elif command == "CODING":
        coffees_num = 2
        total_coffees += coffees_num



    if command == 'dog':
        coffees_num = 1
        total_coffees += coffees_num
    elif command == "DOG":
        coffees_num = 2
        total_coffees += coffees_num
    elif command == 'cat':
        coffees_num = 1
        total_coffees += coffees_num
    elif command == "CAT":
        coffees_num = 2
        total_coffees += coffees_num


    if command == 'movie':
        coffees_num = 1
        total_coffees += coffees_num
    elif command == "MOVIE":
        coffees_num = 2
        total_coffees += coffees_num

