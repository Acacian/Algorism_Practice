import sys
input = sys.stdin.readline

N,M = map(int,input().split())

def backtrack(depth):
    # 끝나는조건
    if depth == M:
        print(' '.join(map(str, result)))
        return

    # 반복되는조건
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            result[depth] = i
            backtrack(depth + 1)
            visited[i] = False

visited = [False] * (N+1)
result = [0] * M

backtrack(0)
