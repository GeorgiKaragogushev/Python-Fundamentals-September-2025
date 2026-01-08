word = input()
result = []

for index in range(len(word)):

    if word[index].isupper():
        result += [index]
print(result)
