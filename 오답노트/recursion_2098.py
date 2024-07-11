import sys
input = sys.stdin.readline
from functools import lru_cache

# 도시 수 입력받기
city = int(input())
W = []
for _ in range(city):
    W.append(list(map(int, input().split())))

# lru_cache를 사용해 메모이제이션
@lru_cache(None)
def tsp(current, visited):
    # 모든 도시를 방문한 경우, 출발 도시로 돌아갈 수 있는지 확인
    if visited == (1 << city) - 1:
        return W[current][0] if W[current][0] > 0 else float('inf')
    
    min_cost = float('inf')
    for next_city in range(city):
        # 다음 도시를 방문하지 않았고, 현재 도시에서 다음 도시로 갈 수 있는 경우
        if not visited & (1 << next_city) and W[current][next_city] != 0:
            min_cost = min(min_cost, tsp(next_city, visited | (1 << next_city)) + W[current][next_city])
    
    return min_cost

# 시작 도시(0번 도시)를 방문한 상태로 시작
result = tsp(0, 1)
print(result)