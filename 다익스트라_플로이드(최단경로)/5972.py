from collections import defaultdict
import heapq

# N = 노드 M = 간선
A = list(map(int, input().split()))
N, M = A[0], A[1]

# start, end, cost
graph = defaultdict(list)
li = []
for i in range(M):
    li.append(list(map(int, input().split())))

def answer():
    for load in li:
        graph[load[0]].append([load[2],load[1]])
        graph[load[1]].append([load[2],load[0]])

    costs = {}
    pq = []
    heapq.heappush(pq, (0,1))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_node in costs:
            continue
        costs[cur_node] = cur_cost

        for cost, next_node in graph[cur_node]:
            if next_node not in costs:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_node,next_cost))
    return costs.get(N,-1)

print(answer())