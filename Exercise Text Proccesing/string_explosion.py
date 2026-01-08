string = input()
strenght = 0
final_string = ''

for index in range(len(string)):
    if strenght > 0 and string[index] != '>':
        strenght -= 1
    elif string[index] == '>':
        final_string += '>'
        strenght += int(string[index + 1])
    else:
        final_string+= string[index]

print(final_string)
