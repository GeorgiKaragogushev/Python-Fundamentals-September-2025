numbers = input().split()
integers = []

for num in numbers:
    integers.append(int(num))

def sorted_nums ():
    print(sorted(integers))

sorted_nums()