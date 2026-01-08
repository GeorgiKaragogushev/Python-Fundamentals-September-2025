messages = input().split()
result = []
for message in messages:
    message = [element for element in message]
    numbers_in_message = ''
    for i in range(len(message)):
        if message[i].isdigit():
            numbers_in_message += message[i]
        else:
            break

    message = [chr(int(numbers_in_message))] + message[i:]
    message[1],message[-1] = message[-1],message[1]
    result.append(''.join(message))
print(' '.join(result))