import sys

input = sys.stdin.readline

# 입력 받기
N, M, B = map(int, input().split())

# 땅의 높이 정보 입력 받기
land = [list(map(int, input().split())) for _ in range(N)]

# 최소, 최대 높이 찾기
min_height = min(min(row) for row in land)
max_height = max(max(row) for row in land)

min_time = float('inf')  # 최소 시간
final_height = 0  # 최종 높이

# 가능한 모든 높이에 대해 시뮬레이션
for h in range(min_height, max_height + 1):
    time = 0  # 현재 높이로 만드는 데 걸리는 시간
    inventory = B  # 현재 인벤토리의 블록 수
    
    # 모든 땅에 대해 반복
    for i in range(N):
        for j in range(M):
            diff = land[i][j] - h  # 현재 땅과 목표 높이의 차이
            if diff > 0:  # 땅이 더 높은 경우
                time += diff * 2  # 블록 제거 (2초 소요)
                inventory += diff  # 인벤토리에 블록 추가
            elif diff < 0:  # 땅이 더 낮은 경우
                time -= diff  # 블록 추가 (1초 소요, diff가 음수이므로 뺄셈)
                inventory += diff  # 인벤토리에서 블록 제거 (diff가 음수)
    
    # 인벤토리의 블록이 음수가 아니고 (충분한 블록이 있고)
    # 현재 시간이 이전까지의 최소 시간보다 작거나 같으면 업데이트
    if inventory >= 0 and time <= min_time:
        min_time = time
        final_height = h

# 결과 출력: 최소 시간과 그때의 땅 높이
print(min_time, final_height)