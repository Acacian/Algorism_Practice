import sys
input = sys.stdin.readline

a1,a0 = map(int,input().split())
c = int(input())
n0 = int(input())
# 식
# a1 * c + a0 >= n0 * c 이 상황이 한 번이라도 있을 시 0, 아니면 1
# => a0 > 0일 때, al >= n0일 시 무조건 0이 된다는 뜻.
# 문제 아래에서도 나온 것처럼 그냥 수학문제다.

if a1 > c:
    print(0)
elif a1 == c:
    print(1 if a0 <= 0 else 0)
else:  # a1 < c
    print(1 if a1 * n0 + a0 <= c * n0 else 0)