
def char_in_range (str_one,str_two):
    my_list = []
    for num in range(ord(str_one)+1, ord(str_two)):
        my_list.append(chr(num))
    return my_list

first = input()
second = input()

result = char_in_range(first,second)
print(' '.join(result))

