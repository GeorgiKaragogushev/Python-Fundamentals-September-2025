storage = {}
current_line_count = 0
resources = []
quantity = []

while True:
    resource = input()
    if resource == 'stop':
        break
    quantity_count = int(input())

    resources.append(resource)
    quantity.append(quantity_count)

for key, value in zip(resources, quantity):
    if key not in storage:
        storage[key] = int(value)
    else:
        storage[key] += int(value)

for key, value in storage.items():
    print(f'{key} -> {value}')
