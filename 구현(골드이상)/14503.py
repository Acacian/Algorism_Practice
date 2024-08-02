## 미완 > 내일 bfs로 풀거임

# 방 크기
Big = list(map(int,input().split()))
N,M = Big[0],Big[1]
# 로봇청소기위치
destination = list(map(int,input().split()))
r,c,dest = destination[0],destination[1],destination[2]
# 방 구조
Room = []
for i in range(N):
    Room.append(list(map(int,input().split())))

# 로봇이 움직이는 환경 구성
# 4방향 확인 / 청소할 칸 없으면 한 칸 후진 / 청소할 칸 있으면 90도 돌면서 이동
# 만약 후진했는데 벽이면 작동 중지
# r,c에 + 1 해서 처음에 인덱스 추가 안 해도 됨
# 벽 : 1 / 청소 안 한곳 : 0 / 청소 한 곳 : -1
def RobotCleaner(x,y,m,ct):
    # 4방향 검사
    if x > 0 and x < M-1 and y > 0 and y < N-1 and Room[x+1][y] == 0 or Room[x-1][y] == 0 or Room[x][y+1] == 0 or Room[x][y-1] == 0:
        m += 1

        if m > 3:
            m = 0

        if m == 0 and Room[x][y-1] == 0:
                Room[x][y-1] = -1
                RobotCleaner(x,y-1,m,ct+1)
        elif m == 1 and Room[x+1][y] == 0:
                Room[x+1][y] = -1
                RobotCleaner(x+1,y,m,ct+1)
        elif m == 2 and Room[x][y+1] == 0:
                Room[x][y+1] = -1
                RobotCleaner(x,y+1,m,ct+1)
        elif m == 3 and Room[x-1][y] == 0:
                Room[x-1][y] = -1
                RobotCleaner(x-1,y,m,ct+1)
        else:
            RobotCleaner(x,y,m,ct)

    # 검사 다 했는데 없음
    # 뒤에 벽 있으면 ct를 반환/아니면 한 칸 후진
        if m == 0:
            if Room[x][y+1] == 1:
                return ct 
            else:
                if Room[x][y+1] == 0:
                    Room[x][y+1] = -1
                    RobotCleaner(x,y+1,m,ct+1)
                else:
                    RobotCleaner(x,y+1,m,ct)
        elif m == 1:
            if Room[x-1][y] == 1:
                return ct 
            else:
                if Room[x-1][y] == 0:
                    Room[x-1][y] = -1
                    RobotCleaner(x-1,y,m,ct+1)
                else:
                    RobotCleaner(x-1,y,m,ct)
        elif m == 2:
            if Room[x][y-1] == 1:
                return ct 
            else:
                if Room[x][y-1] == 0:
                    Room[x][y-1] = -1
                    RobotCleaner(x,y-1,m,ct+1)
                else:
                    RobotCleaner(x,y-1,m,ct)
        elif m == 3:
            if Room[x+1][y] == 1:
                return ct 
            else:
                if Room[x+1][y] == 0:
                    Room[x+1][y] = -1
                    RobotCleaner(x+1,y,m,ct+1)
                else:
                    RobotCleaner(x+1,y,m,ct)

print(RobotCleaner(r,c,dest,0))