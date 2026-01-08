import re
text = input()
bought_items = []
total_sum = 0

while text != 'Purchase':


    pattern = r'>{2}([A-Za-z]+)<{2}(\d+\.?\d*)!(\d+)'
    match = re.findall(pattern,text)
    if match:
        for item in match:
            bought_items.append(item[0])

            total_sum += float(item[1]) * int(item[2])
    text = input()

print('Bought furniture:')
for product in bought_items:
    print(product)

print(f'Total money spend: {total_sum:.2f}')