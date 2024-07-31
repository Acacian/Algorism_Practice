from collections import deque

li = list(map(str, input().split("-")))

# 맨 앞이 음수일 경우를 고려해야 함
if li[0] == '':
    li[0] = "0"

for i in range(len(li)):
    if "+" in li[i]:
        K = li[i].split("+")
        sum = 0
        for j in range(len(K)):
            sum += int(K[j])
        li[i] = sum
    else:
        li[i] = int(li[i])

ans = li[0]
if len(li) == 1:
    print(*li)
else:
    for k in range(1,len(li)):
        ans = ans - li[k]
    print(ans)
