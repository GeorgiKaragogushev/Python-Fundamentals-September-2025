message = input()
storage = {}

for i in message:
    if i == ' ':
        continue
    if i not in storage:
        storage[i] = 1
    else:
        storage[i] +=1

for key,value in storage.items():
    print(f'{key} -> {value}')

