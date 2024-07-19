import sys
input = sys.stdin.readline

T = int(input())

def kantore(x):
    # 예외처리조건
    if x == 0:
        return 0

    # 작대기 길이
    row = "-" * (3 ** x)



    return row
        
for _ in range(T):
    num = int(input())
    print(kantore(num))