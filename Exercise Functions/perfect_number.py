def is_perfect(some_number: int):
    divisors_num = 0
    for devisor in range(1,some_number):
        if some_number % devisor == 0:
            divisors_num += devisor
    if divisors_num == some_number:
        return 'We have a perfect number!'
    return "It's not so perfect."


number = int(input())
print(is_perfect(number))

