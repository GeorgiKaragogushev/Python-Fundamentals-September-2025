text = input()
final_string = ''

for index in range(len(text)):
    if index + 1 < len(text):
        if text[index] !=  text[index + 1]:
            final_string += text[index]
    elif index + 1 == len(text):
        final_string += text[index]

print(final_string)