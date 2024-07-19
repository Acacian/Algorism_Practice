import sys
input = sys.stdin.readline

N, r, c = map(int, input().split())

    # 저장용 ans 변수 추가
    # 초기값을 1로 잡아야 계산하기 편할 것 같다
    # 생각을 바꿈. 확장하는 게 아니라 DP처럼 큰 Z에서 작은 Z로 쪼개야 함
    # 총 네모 크기는 2의 c승이므로, 이걸 4등분해서 해결방안 생성
    # 종료 조건이 어디에 있든 이전에 지나친 값들은 컴퓨터에 의해 전부 계산했다고 가정
def Z(n, r, c):
    if n == 0:
        return 0
    
    half = 2**(n-1)
    quad = half * half

    if r < half and c < half:  # 1사분면
        return Z(n-1, r, c)
    elif r < half and c >= half:  # 2사분면
        return quad + Z(n-1, r, c-half)
    elif r >= half and c < half:  # 3사분면
        return 2*quad + Z(n-1, r-half, c)
    else:  # 4사분면
        return 3*quad + Z(n-1, r-half, c-half)

print(Z(N, r, c))