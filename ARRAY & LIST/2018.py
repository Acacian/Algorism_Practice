import sys
input = sys.stdin.readline

N = int(input())
# 전체부터 세는 게 아니라 절반 잘라서 거기까지만 세게 함
# 만약 홀수라면 큰 값까지 카운트
if N % 2 == 1:
    NN = N // 2 + 1
else:
    NN = N // 2

count = 0
for i in range(1,NN+1):
    ans = 0
    for j in range(i, NN+1):
        ans = ans + j
        if ans > N:
            break
        elif ans == N:
            count += 1
            break

# 지 자신도 세야하니까 + 1(맨 마지막)
# 단, 1일 때는 제외
if N >= 2:
    count += 1

print(count)




