import sys
input = sys.stdin.readline
N = int(input())

# 문제에 DP랑 그리디 써져있는거보니 그냥 두뇌문제
# 5로 나눠 보고, 나머지 3이면 상관 X / 3 아니면 5 한번 or 2번까지 빼 봄
# (3과 5의 최소공배수가 15이기 때문에 어짜피 그 안에서 해결됨)
# 소수 : 1,2,4,7,11 ... 근데 11부터는 3,5로 구현 가능함 > 1,2,4,7 나오면 - 1
# 나머지를 저장하는 변수 A
A = 0
if N == 1 or N == 2 or N == 4 or N == 7:
    print(-1)
elif N % 5 == 3:
    print((N // 5) + 1)
elif N % 5 != 3:
    # 순수 3의 배수인지 확인
    if N % 3 == 0:
        print(N // 3)
    # 순수 3의 배수가 아니라면, 나머지가 3의 배수인지 확인
    else:
        A = (N % 5) + 5
        if A % 3 == 0:
            print((A // 3) + ((N // 5) - 1))
        elif A % 3 != 0:
            A = (N % 5) + 5
            print((A // 3) + ((N // 5) - 2))






