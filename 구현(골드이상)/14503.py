from collections import deque

# 방 크기
N, M = map(int, input().split())
# 로봇청소기 위치와 방향
r, c, dest = map(int, input().split())
# 방 구조
Room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

# 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def RobotCleaner(x, y, m):
    # 현재 위치 청소
    if visited[x][y] == 0:
        visited[x][y] = 1

    for _ in range(4):
        # 왼쪽으로 회전
        m = (m + 3) % 4
        ddx = x + dx[m]
        ddy = y + dy[m]
        if 0 <= ddx < N and 0 <= ddy < M and Room[ddx][ddy] == 0 and visited[ddx][ddy] == 0:
            RobotCleaner(ddx, ddy, m)
            return
        
    # 네 방향 모두 청소가 되어 있거나 벽인 경우
    # 후진
    back = (m + 2) % 4
    bx = x + dx[back]
    by = y + dy[back]
    if 0 <= bx < N and 0 <= by < M and Room[bx][by] == 0:
        RobotCleaner(bx, by, m)
    else:
        # 후진할 수 없으면 종료
        return

# 청소 시작
RobotCleaner(r, c, dest)

# 청소한 영역의 수 출력
cleaned_count = sum(sum(row) for row in visited)
print(cleaned_count)
