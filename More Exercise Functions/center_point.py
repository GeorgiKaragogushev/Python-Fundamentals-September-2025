from math import floor

def closest_to_center(x_num,y_num):
    return abs(x_num) + abs(y_num)


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

first_coorsds = closest_to_center(x1,y1)
second_coords = closest_to_center(x2,y2)

if first_coorsds >= second_coords:
    print(f"({floor(x2)}, {floor(y2)})")
else:
    print(f"({floor(x1)}, {floor(y1)})")




