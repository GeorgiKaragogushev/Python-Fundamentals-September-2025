key = int(input())
number_of_lines = int(input())

new_letter = ''
new_word = ''


for line in range(number_of_lines):
    letter = input()

    new_letter = chr(ord(letter) + key)

    new_word+= new_word.join(new_letter)

print(new_word)



