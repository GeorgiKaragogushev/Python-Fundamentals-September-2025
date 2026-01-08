sequence_of_strings = input().split()
result = ''

for word in sequence_of_strings:
    result += word*len(word)


print(result)