number_messages = int(input())


for message in range(number_messages):
    number = int(input())
    message_by_number = ''

    if number == 88:
        message_by_number = 'Hello'

    elif number == 86:
        message_by_number = 'How are you?'

    elif number > 88:
        message_by_number = 'Bye.'

    elif number != 88 and number != 86:
        message_by_number = 'GREAT!'


    print(message_by_number)