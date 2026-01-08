text = input()
result = ''
substring = ''
repetitions = ''

for index in range(len(text)):
    if not text[index].isdigit():
        substring += text[index].upper()
    else:
        repetitions += text[index]
        if index + 1 < len(text):
            if text[index + 1].isdigit():
                repetitions += text[index + 1]
        result += substring * int(repetitions)
        substring = ""
        repetitions = ''

print(f'Unique symbols used: {len(set(result))}')
print(result)

