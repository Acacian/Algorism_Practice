import sys
import heapq
input = sys.stdin.readline

# 입력 받기
T = int(input())

# deque로도 풀 수 있지 않을까 하다가 시간초과 나서 포기함.. 우선순위큐 나와서
# heapq 쓰라고 말해 준건데 괜히 뻘짓한듯
# 힙 두개 써야 하나? 싶어서 두 개 쓰다가 결국 하나만 썼다.
def fileing():
    num = int(input())
    files = list(map(int, input().split()))
    
    # 모든 파일을 하나의 힙에 넣기
    heap = files
    heapq.heapify(heap)
    
    total_cost = 0
    
    # 힙의 크기가 1보다 클 동안 반복
    while len(heap) > 1:
        # 가장 작은 두 파일 꺼내기
        a = heapq.heappop(heap)
        b = heapq.heappop(heap)
        
        # 두 파일 합치기
        merged = a + b
        total_cost += merged
        
        # 합친 파일을 다시 힙에 넣기
        heapq.heappush(heap, merged)
    
    return total_cost

for _ in range(T):
    print(fileing())