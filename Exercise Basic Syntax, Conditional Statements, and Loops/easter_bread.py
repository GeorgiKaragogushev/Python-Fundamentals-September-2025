budget = float(input())
price_per_kg_flour = float(input())
price_per_pack_eggs = price_per_kg_flour * 0.75
price_per_liter_milk = price_per_kg_flour + (price_per_kg_flour * 0.25)

price_for_loaf = price_per_liter_milk / 4 + price_per_pack_eggs + price_per_kg_flour
colored_eggs = 0
loaves_count = 0

while budget >= price_for_loaf:
    colored_eggs +=3
    loaves_count +=1
    budget-= price_for_loaf

    if loaves_count % 3 == 0:
        colored_eggs -= loaves_count-2

print(f"You made {loaves_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
