import sys
import heapq
input = sys.stdin.readline

# N : 보석수 / K : 가방수
N, K = map(int,input().split())
gem = []
bag = []

gems = []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(gems, (m, v))
for _ in range(K):
    bag.append(int(input()))

# 우선 value별로 정렬
gem.sort(key = lambda x : (x[1]) , reverse= True)
# 작은 가방에 큰 value 가 들어가는 게 좋기 때문에, 가방은 최소값으로 정렬
bag.sort()

# 가방에 담을 수 있으면 담되, 담지 못 한다면 다음 보석으로 넘어감
count = 0
possible_gems = []

for weight in bag:
    while gems and gems[0][0] <= weight:
        m, v = heapq.heappop(gems)
        heapq.heappush(possible_gems, -v)  # 최대 힙을 위해 음수로 저장
    
    if possible_gems:
        count -= heapq.heappop(possible_gems)  # 음수로 저장했으므로 빼기

print(count)

