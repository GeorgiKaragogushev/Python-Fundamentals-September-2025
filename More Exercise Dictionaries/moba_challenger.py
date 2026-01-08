command = input()
players_pool = {}

while command != 'Season end':
    if '->' in command:
        command = command.split(' -> ')
        player = command[0]
        position = command[1]
        skill_points = int(command[2])
        if player not in players_pool:
            players_pool[player] = {}
        if position not in players_pool[player]:
            players_pool[player][position] = skill_points
        elif players_pool[player][position] < skill_points:
            players_pool[player][position] = skill_points

    elif ' vs ' in command:
        player_one, player_two = command.split(' vs ')
        if player_one in players_pool and player_two in players_pool:
            for current_position in players_pool[player_one]:
                if current_position in players_pool[player_two]:
                    if players_pool[player_one][current_position] < players_pool[player_two][current_position]:
                        del players_pool[player_one]
                        break
                    else:
                        del players_pool[player_two]
                        break

    command = input()

for name, info in sorted(players_pool.items(),key=lambda x: -sum(x[1].values())):
    total_points = sum(players_pool[name].values())
    print(f'{name}: {total_points} skill')
    for current_position, points in sorted(info.items(), key=lambda x: (-x[1], x[0])):
        print(f'- {current_position} <::> {points}')
