import sys
input = sys.stdin.readline
# 참외 개수 K
K = int(input())

li = []
# 밭이 육각형이라고 명시했기 때문에 range에는 6 넣으면 됨
for _ in range(6):
    li.append(list(map(int, input().split())))

# 2와 1은 대칭되며, 4와 3은 대칭됨. 둘 중 하나는 다른 맞은편 두 개의 합
# 작은 네모를 구하는 방법은 3-1-3-1 이렇게 나올 때 그 중간의 곱(1*3)
# 우선 순회를 해야 함
# 각 변마다 길이를 찾아서, 높이와 좌우의 최대 길이를 알아내는게 목표
maxside = 0
maxhigh = 0
side = 0
for i in range(6):
    test = li[i][0]
    test1 = li[i-1][0]
    test2 = li[i-2][0]
    test3 = li[i-3][0]
    #최대넓이 구하기
    if (li[i][0] == 1 or li[i][0] == 2) and li[i][1] > maxside:
        maxside = li[i][1]
    elif (li[i][0] == 3 or li[i][0] == 4) and li[i][1] > maxhigh:
        maxhigh = li[i][1]
    #사이드 넓이 구하기
    # 1 3 1 3 2 4
    if li[i-2][0] == li[i][0] and li[i-3][0] == li[i-1][0]:
        side = li[i-1][1] * li[i-2][1]
    # -로 가면 역순으로 가기때문에 상관 X

    # 1 3 1 4 2 3
    # elif (li[i-2][0] == li[i][0] and li[i-3][0] != li[i-1][0]) or (li[i-2][0] != li[i][0] and li[i-3][0] == li[i-1][0]):
    #     side = li[i-2][1] * li[i-3][1]
    # 3 2 4 1 3 2
    # elif i > 1 and (li[i-5][0] == li[i-1][0] and li[i-4][0] == li[i][0]):
    #     side = li[i][1] * li[i-5][1]

square = (maxside * maxhigh) - side
print(K * square)





