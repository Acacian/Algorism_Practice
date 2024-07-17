import sys
input = sys.stdin.readline

# A : 아픈 손가락 B : 셀 수 있는 수
A = int(input())
B = int(input())

# 각 손가락 사이 별 term 계산은 이렇다
# 예를 들어 사이 손가락이 1개일 경우 1 / 2개일 경우 1 + (2*1) / 3개일 경우 1 + (2*2)
# 그리고 한 바퀴를 도는 건 8번이 걸린다. 단, 양 끝 손가락이 아닐 경우 한 번 더 왕복한다.
# 즉 양 끝 손가락인지 아닌지 여부가 중요하다.
# 양 끝 손가락이라 할지라도 5번 손가락일 경우, 처음부터의 4번을 더해줘야 한다.
if A == 1:
    # 시작도 할 수 없는 경우는 A가 1이고 B가 0인 경우인데, 이는 알아서 0이 나오게 됨
    print(B * 8)
elif A == 5:
    print((B * 8) + 4)
else:
    # 총 순회 횟수 + 처음부터의 횟수 + (홀수일 시)남은 순회
    if B % 2 == 0:
        print(((B // 2) * 8) + (A-1))
    if B % 4 == 1 and A == 2:
        print(((B // 2) * 8) + (A-1) + 6)
    if B % 4 == 3 and A == 2:
        print(((B // 2) * 8) + (A-1) + 6)
    if B % 4 == 1 and A == 4:
        print(((B // 2) * 8) + (A-1) + 2)
    if B % 4 == 3 and A == 4:
        print(((B // 2) * 8) + (A-1))
    if B % 4 == 1 and A == 3:
        print(((B // 2) * 8) + (A-1) + 4)
    if B % 4 == 3 and A == 3:
        print(((B // 2) * 8) + (A-1) + 4)








