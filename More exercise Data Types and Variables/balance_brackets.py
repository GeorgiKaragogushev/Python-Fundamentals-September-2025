number_of_lines = int(input())

opened = False
is_balanced = True

for line in range(number_of_lines):
    text_message = input()

    if text_message != '(' and text_message != ')':
        continue

    elif text_message == '(':
        if opened:
            is_balanced = False
            break
        opened = True

    elif text_message == ')':
        if not opened:
            is_balanced = False
            break
        opened = False

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')


