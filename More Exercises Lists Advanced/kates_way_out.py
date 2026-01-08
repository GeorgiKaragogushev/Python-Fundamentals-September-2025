# Четем броя редове
rows = int(input())

# Четем лабиринта ред по ред и го превръщаме в списък от списъци
maze = [list(input()) for _ in range(rows)]

# Намираме къде е Кейт
for r in range(rows):
    for c in range(len(maze[r])):
        if maze[r][c] == 'k':
            start_r, start_c = r, c

# Таблица, която пази къде сме били
visited = [[False] * len(maze[0]) for _ in range(rows)]

# Глобални променливи за най-дългия път и дали има изход
max_moves = 0
found_exit = False

# Функция за обхождане на лабиринта (DFS)
def walk(r, c, moves):
    global max_moves, found_exit

    # Ако сме на ръба → изход
    if r == 0 or c == 0 or r == rows - 1 or c == len(maze[0]) - 1:
        found_exit = True
        if moves > max_moves:
            max_moves = moves

    # Маркираме клетката като посетена
    visited[r][c] = True

    # Опитваме 4 посоки: нагоре, надолу, наляво, надясно
    directions = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < len(maze[0]):
            if not visited[nr][nc] and maze[nr][nc] == ' ':
                walk(nr, nc, moves + 1)

    # Backtracking
    visited[r][c] = False

# Стартираме от Кейт с moves = 1
walk(start_r, start_c, 1)

# Отпечатваме резултата
if found_exit:
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")
