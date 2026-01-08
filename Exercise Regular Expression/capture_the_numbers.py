import re

string = input()
numbers = []

while string:
    pattern = r'\d+'

    matches = re.findall(pattern, string)

    numbers.append(matches)
    string = input()
print(numbers)
