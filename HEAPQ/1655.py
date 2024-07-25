import heapq
import sys
input = sys.stdin.readline

N = int(input())
left = [] # 최대값 저장(left)
right = [] # 최소값 저장(right)
for _ in range(N):
    num = int(input())
    # 인덱스값으로는 못 뺀다.
    # 헤매다가 결국 구글링했고 heap 2개로 푼다는 걸 알게됨
    
    # 완전트리의 좌우균형을 맞춰주는 법
    if len(left) == len(right):
        heapq.heappush(left, -num)
    else:
        heapq.heappush(right, num)
    
    # 큰 num이 max값 heap으로 갔을 때 서로 swap
    if right and -left[0] > right[0]:
        left_max = -heapq.heappop(left)
        right_min = heapq.heappop(right)
        heapq.heappush(left, -right_min)
        heapq.heappush(right, left_max)

    print(-left[0])