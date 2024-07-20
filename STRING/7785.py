import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(str, input().split())))

# 해시맵 사용
E = []

for i in range(n):
    if li[i][1] == "enter":
        E.append(li[i][0])
    else:
        E.remove(li[i][0])

E.sort(reverse=True)

for i in range(len(E)):
    print(E[i])


