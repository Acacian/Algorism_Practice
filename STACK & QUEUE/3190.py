from collections import deque
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
N = int(input())
K = int(input())
apple = []
for _ in range(K):
    apple.append(list(map(int, input().split())))
direction = deque()
L = int(input())
for _ in range(L):
    direction.append(list(map(str,input().split())))
# print(apple,direction)

# 그럼 어떻게 풀어야할까?
# 만약 큐로만 풀게 되면, 90도 바뀌는 건 어떻게 구현하지?
# 일단 머리 위치를 큐에 넣는다면?
snake = deque()

# 끝나는 경우
count = 0

game_end = False
# for문으로 해보려 했으나, 너무 복잡해짐을 파악 > 방향전환 때문에라도 DFS를 통한 재귀로 바꿈
def miro(y,x,count,WASD):
        global game_end
        
        if game_end == False:
            # 몸박 카운터
            if [y,x] in snake:
                game_end = True
                return(count)
            # 벽
            if y > N or x > N or y < 1 or x < 1:
                game_end = True
                return(count)

            # 추가 조건일 경우 추가
            if [y,x] not in snake:
                snake.appendleft([y,x])

            # 사과 먹은 걸 반영
            if [y,x] in apple:
                apple.remove([y,x])
            # 지나간 자리를 pop하되, 사과를 얼마나 먹었는가 반영(K+1 - len(apple))
            # snake 길이로 확인하면 될듯
            else:
                snake.pop()

            # 방향전환
            if len(direction) >= 1 and str(count) == direction[0][0]: # 어짜피 순서대로라 정렬안해도됨
                last_direc = direction.popleft() # 방향전환시켰으면 삭제
                if last_direc[1] == "D":
                    WASD += 1
                elif last_direc[1] == "L":
                    WASD -= 1
            
            # 종료조건에 해당하지 않는다면 순회 계속
            if WASD < 0:
                WASD = 3
            if WASD > 3:
                WASD = 0

            if WASD == 0:
                return miro(y,x+1,count+1,0)
            elif WASD == 1:
                return miro(y+1,x,count+1,1)
            elif WASD == 2:
                return miro(y,x-1,count+1,2)
            elif WASD == 3:
                return miro(y-1,x,count+1,3)

print(miro(1,1,0,0))