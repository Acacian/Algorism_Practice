N = int(input())
li = list(map(int,input().split()))
memo = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(i):
        if li[j] < li[i]:
            memo[i] = max(memo[i], memo[j] + 1)

print(max(memo))