ratations = int(input())

for rotation in range(ratations):
    word = input()

    for letter in word:

        if letter == ',' or letter == '.' or letter == '_':
            print(f'{word} is not pure!')
            break

    else:
        print(f'{word} is pure.')

