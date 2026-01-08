people_count = int(input())
wagons = [int(number) for number in input().split()]
max_people_in_wagon = 4

for i in range(len(wagons)):
        current_wagon_left_space  = max_people_in_wagon - wagons[i]
        if people_count >= current_wagon_left_space:
            wagons[i] += current_wagon_left_space
            people_count -= current_wagon_left_space
        else:
            wagons[i] += people_count
            people_count  = 0
            break

if people_count <= 0 and any(w < 4 for w in wagons):
    print(f"The lift has empty spots!")
    print(" ".join([str(wagon) for wagon in wagons]))
elif people_count > 0 and all(w == 4 for w in wagons):
    print(f"There isn't enough space! {people_count} people in a queue!")
    print(" ".join([str(wagon) for wagon in wagons]))
else:
    print(" ".join([str(wagon) for wagon in wagons]))





