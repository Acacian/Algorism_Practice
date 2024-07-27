from collections import deque

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    sheep = 0
    wolf = 0

    while queue:
        x, y = queue.popleft()

        if field[x][y] == 'v':
            wolf += 1
        elif field[x][y] == 'k':
            sheep += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and not visited[nx][ny] and field[nx][ny] != '#':
                visited[nx][ny] = True
                queue.append((nx, ny))

    return (sheep, 0) if sheep > wolf else (0, wolf)

# Input reading
R, C = map(int, input().split())
field = [list(input().strip()) for _ in range(R)]
visited = [[False] * C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

total_sheep = 0
total_wolf = 0

for i in range(R):
    for j in range(C):
        if not visited[i][j] and field[i][j] != '#':
            result = bfs(i, j)
            total_sheep += result[0]
            total_wolf += result[1]

print(total_sheep, total_wolf)
