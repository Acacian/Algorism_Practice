# 이거 모든 예제 + 질문게시판에 있는 반례 통과하는데 틀렸다고 하는 이유를 모르겠음
import sys
input = sys.stdin.readline

N,M = map(int,input().split())
li = []
six,one = 1e9,1e9
for _ in range(M):
    s,o = map(int,input().split())
    if o < one:
        one = o
    if s < six:
        if s > one * 6:
            six = one * 6
        else:
            six = s

# 최소값.. 
ans = 0
ans += min((N // 6) * six , (N // 6) * (one * 6))

if (N % 6) * one > six:
    ans += six
else:
    ans += one * (N % 6) 

print(int(ans))