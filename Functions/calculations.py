def calculation(operator, num1, num2):
    result = 0
    if operator == 'multiply':
        result = num1 * num2

    elif operator == "divide":
        result = int(num1 / num2)

    elif operator == "add":
        result = num1 + num2

    elif operator == "subtract":
        result = num1 - num2
    return result

operator_ = input()
num1_ = int(input())
num2_ = int(input())


new_result = calculation(operator_, num1_, num2_)
print(new_result)
