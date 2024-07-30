import sys
input = sys.stdin.readline

# 상근이가 가지고 있는 카드의 개수
N = int(input())
# 상근이의 카드 번호들
SG = set(map(int, input().split()))
# 확인해야 할 숫자의 개수
M = int(input())
# 확인해야 할 숫자들
ALL = list(map(int, input().split()))

# 결과를 저장할 리스트
result = []

# ALL의 각 숫자에 대해 상근이의 카드 중에 있는지 확인
for num in ALL:
    if num in SG:
        result.append(1)
    else:
        result.append(0)

# 결과 출력
print(*result)