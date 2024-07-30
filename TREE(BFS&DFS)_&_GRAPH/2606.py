import sys
from collections import deque
input = sys.stdin.readline

#컴퓨터수
N = int(input())
#간선수
M = int(input())
#연결
def troy():
    # graph a b
    moved = [[] for _ in range(N+1)]
    for _ in range(M):
        li = (list(map(int, input().split())))
        moved[li[0]].append(li[1])
        moved[li[1]].append(li[0])

    # 처음 인덱스 0값 무시할거라서 하나 더 추가
    visited = [-1 for _ in range(N + 1)]
    queue = deque([1])
    visited[1] = 1

    while queue:
        cur = queue.popleft()
        for next in moved[cur]:
            if visited[next] == -1: #방문 안 했으면
                visited[next] = visited[cur] + 1
                queue.append(next)

    # 0인 visited 찾아서 count
    count = -1 # 1번 제외
    for i in range(1,N+1):
        if visited[i] != -1:
            count += 1
    print(count)

troy()