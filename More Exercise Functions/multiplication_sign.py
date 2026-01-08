def multiplication_result(first,second,third):
    numbers_list = [first,second,third]
    negative_count = 0
    for number in numbers_list:
        if number < 0:
            negative_count +=1
        if number == 0:
            return 'zero'

    if negative_count % 2 == 0:
        return 'positive'
    else:
        return 'negative'



first_number = int(input())
second_number = int(input())
third_number = int(input())

print(multiplication_result(first_number,second_number,third_number))
