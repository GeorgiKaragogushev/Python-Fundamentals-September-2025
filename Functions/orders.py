def order(product, quantity):
    result = 0
    if product == "coffee":
        result = 1.50 * quantity

    elif product == "water":
        result = 1.00 * quantity

    elif product == 'coke':
        result = 1.40 * quantity

    elif product == 'snacks':
        result = 2.00 * quantity

    return result


product_ = input()
quantity_ = int(input())

final_result = order(product_, quantity_)
print(f'{final_result:.2f}')
