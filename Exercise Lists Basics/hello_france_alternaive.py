items = input().split('|')
budget = float(input())
start_budget = budget

items_recived = []
numbers_list = []
selled_items_sum = 0
bought_item = 0
profit_price = 0

for item in items:
    product = item.split('->')
    product_type,product_value = product[0],float(product[1])

    if product_value > budget:
        continue

    if product_type == 'Clothes':
        if product_value > 50.00:
            continue
        else:
            budget-= product_value

    elif product_type == 'Shoes':
        if product_value > 35.00:
            continue
        else:
            budget-= product_value

    elif product_type == 'Accessories':
        if product_value > 20.50:
            continue
        else:
            budget -= product_value
    else:
        continue

    bought_item += product_value
    selled_item = product_value + (product_value * 0.4)
    selled_items_sum += selled_item
    items_recived.append(f'{selled_item:.2f}')

profit_price = selled_items_sum - bought_item

for num in items_recived:
    numbers_list.append(str(num))
print(' '.join(numbers_list))
print(f'Profit: {profit_price:.2f}')

budget+= selled_items_sum

if budget >= 150:
    print('Hello, France!')
else:
    print('Not enough money.')




