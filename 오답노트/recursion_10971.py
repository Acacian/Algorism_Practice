# 외판원문제(백트래킹, 재귀)

import sys
input = sys.stdin.readline

city = int(input())
W = []
for _ in range(city):
    W.append(list(map(int, input().split())))

# 가장 적은 값을 찾고, 저장함. 그 다음부턴 완탐하는데 조건에 맞지 않을 경우 초기화시킴.
# 0(이미 있는곳) 이랑 갔던 곳은 더 이상 가면 안 됨
visited = [0] * city

def tsp(current, count, cost, start):
    if count == city and W[current][start] != 0:
        return cost + W[current][start] # 종료조건

    min_cost = float('inf') # 1e9랑 똑같은 역할
    for i in range(city):
        if not visited[i] and W[current][i] != 0:
            visited[i] = True
            min_cost = min(min_cost, tsp(i,count + 1,cost + W[current][i], start))
            visited[i] = False
    
    return min_cost

visited[0] = True
result = tsp(0,1,0,0)
print(result)