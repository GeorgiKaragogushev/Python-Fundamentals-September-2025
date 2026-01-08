text = input()
notebook = {}

words_and_definitions = text.split(' | ')
for couple in words_and_definitions:
    word,definitons = couple.split(': ')

    if word not in notebook:
        notebook[word] = []
    notebook[word].append(definitons)

test_words = input().split(' | ')

command = input()
if command == 'Test':
    for word in test_words:
        if word in notebook:
            print(f'{word}:')
            for definition in notebook[word]:
                print(f'-{definition}')
elif command == 'Hand Over':
    print(' '.join(notebook.keys()))
