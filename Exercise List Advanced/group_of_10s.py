def number_groups(num_list):
    group = 10
    while num_list:
        current_numbers = [num for num in num_list if num <= group]
        print(f"Group of {group}'s: {current_numbers}")

        num_list = [num for num in num_list if num >group]
        group += 10


numbers = list(map(int,input().split(', ')))
number_groups(numbers)

