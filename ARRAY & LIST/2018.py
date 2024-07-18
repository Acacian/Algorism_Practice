import sys
input = sys.stdin.readline

N = int(input())
# 전체부터 세는 게 아니라 절반 잘라서 거기까지만 세게 함
# 만약 홀수라면 큰 값까지 카운트
NN = N // 2
if NN % 2 == 1:
    NN = N // 2 + 1

count = 0
for i in range(NN):
    ans = 0
    for j in range(i, NN):
        ans = ans + i
        if ans > N:
            break
        elif ans == N:
            count += 1
            break
print(count)




