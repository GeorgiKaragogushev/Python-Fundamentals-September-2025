
def tax_calculation(current_sum):
    return current_sum * 0.20

total_sum = 0
price_without_taxes = 0
total_tax = 0

while True:
    command = input()
    if command == 'special':
        if not total_sum:
            print("Invalid order!")
            break
        total_sum -= total_sum * 0.10
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {price_without_taxes:.2f}$')
        print(f'Taxes: {total_tax:.2f}$')
        print(f"-----------\nTotal price: {total_sum:.2f}$")
        break

    elif command == 'regular':
        if not total_sum:
            print("Invalid order!")
            break
        print("Congratulations you've just bought a new computer!")
        print(f'Price without taxes: {price_without_taxes:.2f}$')
        print(f'Taxes: {total_tax:.2f}$')
        print(f"-----------\nTotal price: {total_sum:.2f}$")
        break

    price = float(command)

    if price < 0:
        print('Invalid price!')
        continue

    price_without_taxes += price
    total_tax += tax_calculation(price)
    total_sum = price_without_taxes + total_tax

