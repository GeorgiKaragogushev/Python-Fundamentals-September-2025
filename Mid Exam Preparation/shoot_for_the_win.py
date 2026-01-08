target_values = list(map(int, input().split()))
total_shots = 0

while True:
    command = input()

    if command == 'End':
        print(f"Shot targets: {total_shots} -> {' '.join(str(num) for num in target_values)}")
        break

    target_index = int(command)

    if target_index < len(target_values):
        if target_values[target_index] == -1:
            continue

        index_value = target_values[target_index]
        target_values[target_index] = -1
        total_shots += 1

        for i in range(len(target_values)):
            if target_values[i] != -1:
                if target_values[i] > index_value:
                    target_values[i] -= index_value
                else:
                    target_values[i] += index_value
