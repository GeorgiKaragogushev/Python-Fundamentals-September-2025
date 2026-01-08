first_line = input().split()
second_line = input().split()
third_line = input().split()
first_won = False
second_won = False

if (first_line[0] == '1' and first_line[1] == '1' and first_line[2] == '1'
    or second_line[0] == '1' and second_line[1] == '1' and second_line[2] == '1'
    or third_line[0] == '1' and third_line[1] == '1' and third_line[2] == '1'):
    first_won = True
elif (first_line[0] == '1' and second_line[0] == '1' and third_line[0] == '1'
    or first_line[1] == '1' and second_line[1] == '1' and third_line[1] == '1'
    or first_line[2] == '1' and second_line[2] == '1' and third_line[2] == '1'):
    first_won = True
elif first_line[0] == '1' and second_line[1] == '1' and third_line[2] == '1' or first_line[2] == '1' and second_line[1] == '1' and third_line[0] == '1':
    first_won = True

elif (first_line[0] == '2' and first_line[1] == '2' and first_line[2] == '2'
    or second_line[0] == '2' and second_line[1] == '2' and second_line[2] == '2'
    or third_line[0] == '2' and third_line[1] == '2' and third_line[2] == '2'):
    second_won = True
elif (first_line[0] == '2' and second_line[0] == '2' and third_line[0] == '2'
    or first_line[1] == '2' and second_line[1] == '2' and third_line[1] == '2'
    or first_line[2] == '2' and second_line[2] == '2' and third_line[2] == '2'):
    second_won = True
elif first_line[0] == '2' and second_line[1] == '2' and third_line[2] == '2' or first_line[2] == '2' and second_line[1] == '2' and third_line[0] == '2':
    second_won = True




if first_won:
    print('First player won')
elif second_won:
    print('Second player won')
else:
    print('Draw!')