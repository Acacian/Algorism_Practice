from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    positions = list(range(n))
    queue = deque(priorities)
    position_queue = deque(positions)
    count = 0

    while queue:
        if queue[0] == max(queue):
            count += 1
            if position_queue[0] == m:
                print(count)
                break
            queue.popleft()
            position_queue.popleft()
        else:
            queue.append(queue.popleft())
            position_queue.append(position_queue.popleft())

# from collections import deque
# import sys
# input = sys.stdin.readline

# N = int(input())
# for _ in range(N):
#     n, m = map(int, input().split())
#     q = deque(map(int, input().split()))

#     #sort 하려다 맨 마지막 예제때문에 포기
#     while len(q) >= 1 and q[m] in q:
#         count = 0
#         for i in range(0,len(q)):
#             if len(q) == 1 or q[i] >= q[i+1]:
#                 q.popleft()
#                 count += 1
#             else:
#                 q.append(q[i])
#                 for j in range(1,len(q)-1):
#                     q[j-1] = q[j]
#                 q.pop(len(q)-1)
#                 # len(q)-1
#         print(count)
