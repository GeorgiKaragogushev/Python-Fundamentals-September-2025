import re

text = input()

pattern = r'[\*\^]+([A-Za-z\s]{6,})[\*\^]+[^A-Za-z0-9]+(-?\d+(\.\d+)?,-?\d+(\.\d+)?)'

matches = re.findall(pattern,text)
if matches:
    for match in matches:
        artifact_name = match[0]
        coords = match[1]
        print(f'Found {artifact_name} at coordinates {coords}.')
else:
    print('No valid artifacts found.')
