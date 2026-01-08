product_list = input().split()
stock = {}

for i in range(0,len(product_list),2):
    food_type = product_list[i]
    quantity = int(product_list[i+1])
    stock[food_type] = quantity
print(stock)



