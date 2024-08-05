# 다익스트라가 있긴 한데 BFS에 더 가까운 것 같은데?
# 근데 거리계산해야하니 다익스트라도 될지도
from collections import defaultdict
import heapq

N = int(input())
li = []
for _ in range(N):
    li.append(list(map(int,input())))

def answer():
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    pq = []
    heapq.heappush(pq, [0,0,0])
    visited = [[0 for _ in range(N)] for _ in range(N)]
    visited[0][0] = 1

    while pq:
        a,x,y = heapq.heappop(pq)
        if x == N-1 and y == N-1:
            print(a)
            return # 도착
    
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                if li[nx][ny] == 0:
                    heapq.heappush(pq, [a+1,nx,ny])
                else:
                    heapq.heappush(pq, [a,nx,ny])

answer()