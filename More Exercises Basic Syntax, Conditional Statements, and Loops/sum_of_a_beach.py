text = input()
text = text.lower()


total_count = 0
total_count += text.count('sand')
total_count += text.count('fish')
total_count += text.count('sun')
total_count += text.count('water')

print(total_count)