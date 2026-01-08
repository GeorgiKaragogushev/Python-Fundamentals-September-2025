numbers = list(map(int,input().split()))
total_removed_elements_value = 0

while numbers:
    given_index = int(input())

    if given_index < 0:
        removed_element = numbers.pop(0)
        last_number = numbers[-1]
        numbers.insert(0,last_number)
        total_removed_elements_value += removed_element

        for index in range(len(numbers)):
            if numbers[index] <= removed_element:
                numbers[index] += removed_element
            elif numbers[index] > removed_element:
                numbers[index] -= removed_element
    elif given_index >= len(numbers):
        first_number = numbers[0]
        removed_element = numbers.pop(-1)
        numbers.append(first_number)
        total_removed_elements_value += removed_element

        for index in range(len(numbers)):
            if numbers[index] <= removed_element:
                numbers[index] += removed_element
            elif numbers[index] > removed_element:
                numbers[index] -= removed_element
    else:
        removed_element = numbers.pop(given_index)
        total_removed_elements_value += removed_element
        for index in range(len(numbers)):
            if numbers[index] <= removed_element:
                numbers[index] += removed_element
            elif numbers[index] > removed_element:
                numbers[index] -= removed_element

print(total_removed_elements_value)