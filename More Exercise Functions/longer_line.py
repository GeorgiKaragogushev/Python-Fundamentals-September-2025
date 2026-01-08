from  math import floor

def line_sums(first, second, third, four):
    result = abs(first) + abs(second) + abs(third) + abs(four)
    return result

def longer_line(line_one,line_two):
    if line_one >= line_two:
        if abs(first_line_x1) + abs(first_line_y1) <= abs(first_line_x2) + abs(first_line_y2):
            print(f'({floor(first_line_x1)}, {floor(first_line_y1)})({floor(first_line_x2)}, {floor(first_line_y2)})')
        else:
            print(f'({floor(first_line_x2)}, {floor(first_line_y2)})({floor(first_line_x1)}, {floor(first_line_y1)})')

    else:
        if abs(second_line_x1) + abs(second_line_y1) <= abs(second_line_x2) + abs(second_line_y2):
            print(f'({floor(second_line_x1)}, {floor(second_line_y1)})({floor(second_line_x2)}, {floor(second_line_y2)})')
        else:
            print(f'({floor(second_line_x2)}, {floor(second_line_y2)})({floor(second_line_x1)}, {floor(second_line_y1)})')

first_line_x1 = float(input())
first_line_y1 = float(input())
first_line_x2 = float(input())
first_line_y2 = float(input())

second_line_x1 = float(input())
second_line_y1 = float(input())
second_line_x2 = float(input())
second_line_y2 = float(input())


first_line = line_sums(first_line_x1,first_line_y1,first_line_x2,first_line_y2)
second_line = line_sums(second_line_x1,second_line_y1,second_line_x2,second_line_y2)
longer_line(first_line,second_line)





