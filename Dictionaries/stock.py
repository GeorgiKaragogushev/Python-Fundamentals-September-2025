product_list = input().split()
stock = {}

for i in range(0,len(product_list),2):
    food_type = product_list[i]
    quantity = product_list[i+1]
    stock[food_type] = quantity

products_for_search = input().split()

for product in products_for_search:
    if product in stock:
        print(f"We have {stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

