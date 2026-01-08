
stock = {}

while True:
    products_list = input()

    if products_list == 'statistics':
        break
    food,value = products_list.split(': ')
    value = int(value)

    if food in stock:
        stock[food] += value
    else:
        stock[food] = value

print("Products in stock:")
for product,quantity in stock.items():
    print(f'- {product}: {quantity}')

print(f'Total Products: {len(stock)}\nTotal Quantity: {sum(stock.values())}')