number_of_rooms = int(input())
total_free_chairs = 0

for room in range(1, number_of_rooms + 1):
    room_info = input().split()

    chairs = len(room_info[0])
    visitors = int(room_info[1])
    total_free_chairs += chairs - visitors

    if chairs < visitors:
        print(f"{visitors - chairs} more chairs needed in room {room}")

if total_free_chairs >= 0:
    print(f"Game On, {total_free_chairs} free chairs left")
