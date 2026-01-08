dict_of_synonyms = {}
number_lines = int(input())

for _ in range(number_lines):
    word = input()
    synonym = input()

    if word not in dict_of_synonyms:
        dict_of_synonyms[word] = []
    dict_of_synonyms[word].append(synonym)

for key,value in dict_of_synonyms.items():
    print(f'{key} - {", ".join(value)}')
    