elements = input().split()
storage = {}

for element in  elements:
    element = element.lower()
    if element not in storage:
        storage[element] = 1
    else:
        storage[element] += 1

storage = {key: value for key,value in storage.items() if value % 2 != 0}
result = [key for key in storage.keys()]
print(' '.join(result))
