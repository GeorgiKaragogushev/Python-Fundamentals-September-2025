numbers = input().split()
int_list = []

def number ():
    for num in numbers:
        result = round(float(num))
        int_list.append(result)
    return int_list
number()
print(int_list)


