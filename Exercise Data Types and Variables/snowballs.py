import sys

total_snowballs = int(input())
max_value = -sys.maxsize

best_weight = 0
best_time = 0
best_quality = 0
value = 0

for ball in range(total_snowballs):

    snowball_weight = int(input())
    time_needed = int(input())
    quality_of_ball = int(input())


    value = (snowball_weight // time_needed) ** quality_of_ball


    if value > max_value:
        max_value = value

        best_weight = snowball_weight
        best_time = time_needed
        best_quality = quality_of_ball

print(f"{best_weight} : {best_time} = {max_value} ({best_quality})")




