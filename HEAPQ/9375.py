import heapq
import sys
input = sys.stdin.readline

N = int(input())
di = dict()
for i in range(N):
    di.clear()
    M = int(input())
    for j in range(M):
        arr = list(map(str, input().split()))
        if arr[1] in di:
            di[arr[1]] += 1
        else:
            di[arr[1]] = 1

    result = 1
    for count in di.values():
        result *= (count + 1)
    result -= 1
    print(result)