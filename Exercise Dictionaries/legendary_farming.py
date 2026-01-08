materials = {'shards': 0, 'fragments': 0, 'motes': 0}
item_obtained = False

while not item_obtained:
    list_of_materials = input().split()

    for i in range(0, len(list_of_materials), 2):
        quantity = list_of_materials[i]
        material = list_of_materials[i + 1].lower()
        if item_obtained:
            break

        if material not in materials:
            materials[material] = 0
        materials[material] += int(quantity)
        if material in materials:
            if material == 'shards':
                if materials[material] >= 250:
                    materials[material] -= 250
                    item_obtained = True
                    print(f"Shadowmourne obtained!")
            elif material == 'fragments':
                if materials[material] >= 250:
                    materials[material] -= 250
                    item_obtained = True
                    print(f"Valanyr obtained!")
            elif material == 'motes':
                if materials[material] >= 250:
                    materials[material] -= 250
                    item_obtained = True
                    print(f"Dragonwrath obtained!")
    list_of_materials = input().split()

for material, quantity in materials.items():
    print(f'{material}: {quantity}')
