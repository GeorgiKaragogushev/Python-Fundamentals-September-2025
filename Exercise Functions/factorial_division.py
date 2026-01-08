def factorial_number(number):
    for current_number in range(1,number):
        number *= current_number
    return number

first_number = int(input())
second_number = int(input())

result_first_number = factorial_number(first_number)
result_second_number = factorial_number(second_number)

final_result = result_first_number / result_second_number

print(f"{final_result:.2f}")

