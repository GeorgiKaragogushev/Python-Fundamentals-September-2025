def even_or_odd(some_num: str):
    for num in some_num:
        int_num = int(num)
        if int_num % 2 == 0:
            even_list.append(int_num)
        else:
            odd_list.append(int_num)
    return even_list, odd_list


numbers = input()
even_list = []
odd_list = []

even_or_odd(numbers)
result_odd = sum(odd_list)
result_even = sum(even_list)
print(f"Odd sum = {result_odd}, Even sum = {result_even}")
