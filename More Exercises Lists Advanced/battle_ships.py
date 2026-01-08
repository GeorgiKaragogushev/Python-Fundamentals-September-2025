number_of_rows = int(input())
field_rows = []
destroyed_ships = 0

for row in range(number_of_rows):
    field_row = list(map(int,input().split()))

    field_rows.append(field_row)

attacked_squares = input().split()

row_cow_list = [element.split('-') for element in attacked_squares]


for element in row_cow_list:
    row_index = int(element[0])
    col_index = int(element[1])

    if field_rows[row_index][col_index] >= 1:
        field_rows[row_index][col_index] -= 1
        if field_rows[row_index][col_index] == 0:
            destroyed_ships+=1


print(destroyed_ships)