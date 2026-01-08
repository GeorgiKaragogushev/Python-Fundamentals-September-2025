word = input()

no_vowels = [letter for letter in word if letter.lower() not in ['a', 'u', 'o', 'e', 'i']]

print(''.join(no_vowels))
