import re

lines = int(input())
pattern = r'[star]'
atacked_planets = []
destroyed_planets = []
for line in range(lines):
    encrypted_message = input()
    matches = re.findall(pattern, encrypted_message, re.IGNORECASE)
    found_symbols_lenght = len(matches)
    decrypted_word = ''

    decrypted_word += ''.join(chr(ord(symbol) - found_symbols_lenght) for symbol in encrypted_message)

    new_pattern = r'@([A-Za-z]+)[^@\-!:>]*:([\d]+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)'
    planet_info = re.finditer(new_pattern, decrypted_word)
    for match in planet_info:
        planet_name, population, attack_type, soldiers_count = match.groups()
        if attack_type == 'A':
            atacked_planets.append(planet_name)
        elif attack_type == 'D':
            destroyed_planets.append(planet_name)

print(f'Attacked planets: {len(atacked_planets)}')
for planet in sorted(atacked_planets):
    print(f'-> {planet}')
print(f'Destroyed planets: {len(destroyed_planets)}')
for planet in sorted(destroyed_planets):
    print(f'-> {planet}')
