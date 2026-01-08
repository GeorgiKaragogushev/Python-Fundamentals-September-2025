import re
text = input()
pattern = r'(www\.[a-z0-9\-]+\.[a-z\.]+)'

while text:
    match = re.findall(pattern, text, re.IGNORECASE)
    if match:
        print('\n'.join(match))
    text = input()