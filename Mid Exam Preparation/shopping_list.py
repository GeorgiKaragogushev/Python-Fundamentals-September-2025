def urgent_command(products_list, current_item):
    if current_item not in products_list:
        products_list.insert(0, current_item)
    return products_list


def unnecessary_command(products_list, current_item):
    if current_item in products_list:
        products_list.remove(current_item)
    return products_list


def correct_command(products_list, current_old_item, current_new_item):
    if current_old_item in products_list:
        old_item_index = products_list.index(current_old_item)
        products_list[old_item_index] = current_new_item
    return products_list


def rearrange_command(products_list, current_item):
    if current_item in products_list:
        current_item_index = products_list.index(current_item)
        products_list.append(products_list.pop(current_item_index))
    return products_list


groceries_list = input().split('!')
command = input()
while command != 'Go Shopping!':
    command = command.split()
    current_command, item = command[0], command[1]

    if current_command == 'Urgent':
        groceries_list = urgent_command(groceries_list, item)
    elif current_command == 'Unnecessary':
        groceries_list = unnecessary_command(groceries_list, item)
    elif current_command == 'Correct':
        old_item = item
        new_item = command[2]
        groceries_list = correct_command(groceries_list, old_item, new_item)

    elif current_command == 'Rearrange':
        groceries_list = rearrange_command(groceries_list, item)

    command = input()

print(', '.join(groceries_list))
