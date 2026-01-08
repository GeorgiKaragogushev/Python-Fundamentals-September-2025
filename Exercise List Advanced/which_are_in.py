substring = input().split(', ')
words = input().split(', ')
result = []

for sub in substring:
    for word in words:
        if sub in word and sub not in result:
            result.append(sub)

print(result)
