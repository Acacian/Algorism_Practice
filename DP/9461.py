from collections import deque
import sys
input = sys.stdin.readline

# 배열로 나타냈을 때, i - 2, i - 3의 합이 i가 되는 문제
N = int(input())

def wave():
    M = int(input())
    # 1 3개는 고정(그래야 i-2부터 시작할 수 있음)
    memo = deque([1,1,1])

    if M == 1 or M == 2 or M == 3:
        return 1

    for i in range(4,M+1):
        A = memo.popleft()
        B = memo[0]
        memo.append(A+B)

    return memo[2]

for _ in range(N):
    print(wave())