# BFS 문제
import sys
from collections import deque
input = sys.stdin.readline

CASE = int(input())

# def 안에 선언해 놓으면 따로 global 쓸 필요 X
def knight():
    #배열
    matrix = int(input())
    #현재 있는 칸
    now = list(map(int, input().split()))
    now_x , now_y = now[0], now[1]
    #목표 이동 칸
    dest = list(map(int, input().split()))
    dest_x , dest_y = dest[0], dest[1]
    #visited
    visited = [[0 for _ in range(matrix)] for _ in range(matrix)]

    def knightmove(x, y):
        # 나이트의 이동 패턴 수정
        moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
        visited[x][y] = 1
        queue = deque([(x, y, 0)])  # x, y, 이동 횟수

        while queue:
            x, y, count = queue.popleft()
            if x == dest_x and y == dest_y:
                return count  # 목적지 도달 시 이동 횟수 반환

            for dx, dy in moves:
                nx, ny = x + dx, y + dy
                if 0 <= nx < matrix and 0 <= ny < matrix and not visited[nx][ny]:
                    visited[nx][ny] = 1
                    queue.append((nx, ny, count + 1))
        
        return -1  # 도달할 수 없는 경우

    return knightmove(now_x, now_y)

# CASE 별로 투입
for i in range(CASE):
    print(knight())