import sys
input = sys.stdin.readline

T = int(input())

def kantore(x):
    # 예외처리조건
    if x == 0:
        return "-"

    # 작대기 길이
    row = "-" * (3 ** x)
    if x > 0:
        # 이전 단계의 칸토어 집합 생성
        prev = kantore(x - 1)
        
        # 새로운 칸토어 집합 생성
        left = prev
        middle = " " * len(prev)
        right = prev
        
        # 결과 조합
        row = left + middle + right

    return row
        
for _ in range(T):
    num = int(input())
    print(kantore(num))