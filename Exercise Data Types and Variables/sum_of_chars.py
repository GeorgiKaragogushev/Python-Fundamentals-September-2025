number_lines = int(input())
total_score = 0

for char in range(number_lines):
    new_char = input()

    total_score += ord(new_char)

print(f"The sum equals: {total_score}")
