N = int(input())
li = list(map(int,input().split()))
memo = [1 for _ in range(N)]

for i in range(1,N):
    for j in range(i): 
        if li[j] < li[i]: # 좌
            memo[i] = max(memo[i], memo[j] + 1)

memo2 = [1 for _ in range(N)]
for i in range(N-2,-1,-1):
    for j in range(N-1,i,-1): 
        if li[j] < li[i]: # 우
            memo2[i] = max(memo2[i], memo2[j] + 1)

max_length = 0
for i in range(N):
    max_length = max(max_length, memo[i] + memo2[i] - 1)

print(max_length, memo,memo2)