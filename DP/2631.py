N = int(input())
li = []
memo = [1 for _ in range(N)]

for _ in range(N):
    li.append(int(input()))

for i in range(1,N):
    for j in range(i): # 앞 보면서 탐색
        if li[j] < li[i]:
            memo[i] = max(memo[i], memo[j] + 1)

print(N - max(memo))