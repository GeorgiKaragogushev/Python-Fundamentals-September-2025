import re

phone_numbers = input()

pattern = r'\+359\s2\s\d{3}\s\d{4}\b|\+359-\d-\d{3}-\d{4}\b'


matches = re.findall(pattern,phone_numbers)
print(', '.join(matches))
