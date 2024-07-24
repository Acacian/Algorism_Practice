from collections import deque
import sys

input = sys.stdin.readline
N,M = map(int, input().split())

# 이전 문제들처럼 큐 두개 만들예쩡
# 하나는 저장용, 저장 안된건 뒤로 append
li = deque()
ans = []
for i in range(1,N+1):
    li.append(i)

for i in range(N):
    for j in range(M-1):
        pp = li.popleft()
        li.append(pp)
    incount = li.popleft()
    ans.append(incount)

print("<" + ", ".join(map(str, ans)) + ">")