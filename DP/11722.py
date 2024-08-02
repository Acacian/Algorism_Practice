N = int(input())
li = list(map(int,input().split()))
memo = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(i):
        if li[i] < li[j]:
            memo[i] = max(memo[i] , memo[j] + 1) # memoization 내용 전체와 비교

print(max(memo))
