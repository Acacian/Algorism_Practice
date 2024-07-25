# 시간초과남. 배열, 트리를 쓰면 힙큐없이도 되지만, 아래 코드는 아님

# import heapq
import sys
input = sys.stdin.readline

N = int(input())
HT = []
for _ in range(N):
    HT.append(int(input()))
    HT.sort(reverse=True)
    HP = HT.pop()
    if 0 == HP:
        if len(HT) >= 1:
            print(HT.pop())
        else:
            print(0)
    else:
        HT.append(HP)
