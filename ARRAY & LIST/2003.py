import sys
input = sys.stdin.readline

NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]
li = list(map(int, input().split()))

count = 0
# 처음부터 순회하면서 앞부터 더함 > 5 초과 시 그 다음 숫자부터 시작
for i in range(N):
    ans = 0
    for j in range(i, N):
        ans = ans + li[j]
        if ans > M:
            break
        elif ans == M:
            count += 1
            break

print(count)






