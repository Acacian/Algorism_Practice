import sys
input = sys.stdin.readline

T = int(input())
# 확실히 몇 개인지 알 수 있는 건 T밖에 없음

def palindrom(x):
    # 예외처리조건
    if x == 0:
        return 0

    # 무조건 대칭이 되어야 하며, 합이 T보다 크면 더 세지 않는다
    count = 1  # x 자체를 하나의 파티션으로 계산

    for i in range(1, x):
        left = (x - i) // 2
        if left * 2 + i == x:
            count += palindrom(left)

    if x % 2 == 0:
        count += palindrom(x // 2)

    return count
        
for _ in range(T):
    num = int(input())
    print(palindrom(num))