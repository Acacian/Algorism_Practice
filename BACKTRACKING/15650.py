import sys
input = sys.stdin.readline

N,M = map(int,input().split())

# 1부터 시작인데 인덱스는 0부터 시작이니 + 1
visited = [False] * (N+1)
result = [0] * M

def backtracking(depth):
    # 끝나는 조건 : 모든 분기점 탐색
    if depth == M:
        print(" ".join(map(str, result)))
        return
    # 반복되는 조건 : 분기점 탐색
    for i in range(1,N+1):
        if not visited[i] and (depth == 0 or i > result[depth-1]):
            visited[i] = True
            result[depth] = i
            backtracking(depth+1)
            visited[i] = False

backtracking(0)


