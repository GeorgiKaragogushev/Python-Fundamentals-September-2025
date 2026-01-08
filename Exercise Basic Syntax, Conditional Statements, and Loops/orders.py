orders_count = int(input())
total_price = 0

for order in range(orders_count):
    coffee_capsule_price = float(input())
    days = int(input())
    capsules_needed = int(input())

    if (coffee_capsule_price < 0.01
            or coffee_capsule_price > 100
            or days < 1
            or  days > 31
            or capsules_needed < 1
            or capsules_needed > 2000):
        continue

    price_per_order = (coffee_capsule_price * capsules_needed) * days
    print(f"The price for the coffee is: ${price_per_order:.2f}")

    total_price += price_per_order

print(f'Total: ${total_price:.2f}')