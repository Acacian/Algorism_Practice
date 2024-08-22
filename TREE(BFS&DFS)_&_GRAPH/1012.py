import sys
from collections import deque
input = sys.stdin.readline

def bfs(start_x, start_y):
    # 방향 벡터 설정 (상, 하, 좌, 우)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    queue = deque()
    queue.append((start_x, start_y))
    visited[start_y][start_x] = 1  # 시작 지점 방문 처리
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            ddx = x + dx[i]
            ddy = y + dy[i]
            if 0 <= ddx < M and 0 <= ddy < N and visited[ddy][ddx] == 0:
                visited[ddy][ddx] = 1
                if lst[ddy][ddx] == 1:
                    queue.append((ddx, ddy))

N = int(input())
for _ in range(N):
    M, N, K = map(int, input().split())
    lst = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    
    for _ in range(K):
        x, y = map(int, input().split())
        lst[y][x] = 1
    
    worm_count = 0
    for i in range(N):
        for j in range(M):
            if lst[i][j] == 1 and visited[i][j] == 0:
                bfs(j, i)
                worm_count += 1
    
    print(worm_count)
