number_of_electrons = int(input())
shells = []
start_shell = 1

while sum(shells) < number_of_electrons:
    shells.append(2 * start_shell ** 2)
    start_shell += 1

    if sum(shells) > number_of_electrons:
        numbers_higher = sum(shells) - number_of_electrons
        final_shell_result = shells[-1] - numbers_higher
        shells[-1] = final_shell_result

print(shells)
