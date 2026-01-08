import re
line = input()
pattern = r'%([A-Z][a-z]+)%[^%$|]*<(\w+)>[^%$|]*\|(\d+)\|[^%$|]*?(\d+(?:\.\d+)?)\$'

total_price = 0
while line != 'end of shift':
    matches = re.findall(pattern,line)

    for customer_info in matches:
        name = customer_info[0]
        product = customer_info[1]
        count = int(customer_info[2])
        price = float(customer_info[3]) * count

        print(f'{name}: {product} - {price:.2f}')
        total_price += price
    line = input()

print(f'Total income: {total_price:.2f}')