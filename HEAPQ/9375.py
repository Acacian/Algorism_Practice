import heapq
import sys
input = sys.stdin.readline

N = int(input())
di = dict()
M = int(input())
for i in range(N):
    for j in range(M):
        


ended = False
for i in range(T):
    TG = heapq.heappop(HT) # Tallest Giant

    if -TG < H: # 1빠따가 센티보다 작아요
        print("YES")
        print(i)
        heapq.heappush(HT, TG)
        ended = True
        break

    elif -TG == 1: # 1이하로는 줄어들지 않아요
        heapq.heappush(HT, TG)

    else: 
        if TG % 2 != 0:
            TG = (TG // 2) + 1 # 센티보다 크면, 반 줄이고 다시 힙 안에 투입
        else:
            TG = TG // 2
        heapq.heappush(HT, TG)

# 다 돌고 나서 비교
if ended == False:
    TG = heapq.heappop(HT)
    if -TG >= H:
        print("NO")
        print(-TG)
    else:
        print("YES")
        print(T)