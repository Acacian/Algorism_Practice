import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().split())

def bfs(N, K):
    if N >= K:
        return N - K  # N이 K보다 크거나 같으면 빼기만 하면 됨
    
    limit = max(N, K) * 2  # 탐색할 최대 위치 제한
    visited = set()
    queue = deque([(N, 0)])
    visited.add(N)
    
    while queue:
        cur, time = queue.popleft()
        
        if cur == K:
            return time
        
        for next in (cur * 2, cur + 1, cur - 1):
            if 0 <= next <= limit and next not in visited:
                if next == K:
                    return time + 1  # 다음 위치가 K면 바로 반환
                visited.add(next)
                queue.append((next, time + 1))
    
    return -1  # K에 도달할 수 없는 경우

print(bfs(N, K))