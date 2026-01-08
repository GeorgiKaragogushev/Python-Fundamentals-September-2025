timers = input().split()

middle_part = len(timers) // 2

left_part = timers[:middle_part]
right_part = timers[middle_part+1:][::-1]

left_car_time = 0
right_car_time = 0


for i in left_part:
    if i == '0':
        left_car_time -= left_car_time * 0.20
    else:
        left_car_time += int(i)


for i in right_part:
    if i == '0':
        right_car_time -= right_car_time * 0.20
    else:
        right_car_time += int(i)

if right_car_time >= left_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")