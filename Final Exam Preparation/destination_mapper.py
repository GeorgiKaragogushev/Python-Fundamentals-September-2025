import re

text = input()
destinations = []

pattern = r'([=\/])([A-Z][A-Za-z]{2,})\1'

for matches in re.finditer(pattern,text):
    match = matches.group(2)
    destinations.append(match)

total_points = sum([len(place) for place in destinations])

print(f"Destinations: {', '.join(destinations)}")
print(f'Travel Points: {total_points}')
