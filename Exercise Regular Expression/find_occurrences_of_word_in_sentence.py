import re

text = input()
searched_word = input()
found_words = []

pattern = fr'\b{searched_word}\b'

found_words += re.findall(pattern,text,re.IGNORECASE)

print(len(found_words))