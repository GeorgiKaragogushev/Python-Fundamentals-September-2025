sheeps_and_wolf = input().split(', ')
if sheeps_and_wolf[-1] == 'wolf':
    print('Please go away and stop eating my sheep')
else:
    for index in range(-1,-len(sheeps_and_wolf)-1,-1):
        if sheeps_and_wolf[index] == 'wolf':
            sheep_place = abs(index+1)
            print(f'Oi! Sheep number {sheep_place}! You are about to be eaten by a wolf!')

