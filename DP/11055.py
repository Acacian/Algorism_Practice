N = int(input())
li = list(map(int,input().split()))
memo = [1 for _ in range(N)]

for i in range(1,N):
    memo[i] = li[i]
    for j in range(i):
        if li[j] < li[i]: # 이번에는 앞에서 작은 애들이 다 바뀌게 됨
            memo[i] = max(memo[i] , memo[j] + li[i]) # 이전값 + 현재값 vs memo 현재값
        else:
            memo[i] = max(memo[i] , li[i])

print(max(memo))

