import sys
from collections import deque
input = sys.stdin.readline

N, M, K, X = map(int, input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)

# 방문 배열 초기화 (방문 여부와 거리 정보를 동시에 저장)
visited = [-1] * (N + 1)
visited[X] = 0

# BFS
queue = deque([X])
while queue:
    current = queue.popleft()
    
    for next_node in graph[current]:
        if visited[next_node] == -1:
            visited[next_node] = visited[current] + 1
            queue.append(next_node)

# 최단 거리가 K인 도시 찾기
result = [i for i in range(1, N + 1) if visited[i] == K]

# 결과 출력
if result:
    for city in result:
        print(city)
else:
    print(-1)