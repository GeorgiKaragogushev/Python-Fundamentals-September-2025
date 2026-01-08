product_dict = {}

command = input()

while command != 'buy':
    product_info = command.split()
    product,price,quantity = product_info[0], float(product_info[1]),int(product_info[2])
    if product not in product_dict.keys():
        product_dict[product] = {'price': price, 'quantity': quantity}
    else:
        if product_dict[product] != price:
            product_dict[product]['price'] = price
        product_dict[product]['quantity'] += quantity

    command = input()

for product in product_dict:
    price = product_dict[product]['price']
    quantity  = product_dict[product]['quantity']
    price = price * quantity

    print(f'{product} -> {price:.2f}')









