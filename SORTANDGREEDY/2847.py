N = int(input())
li = {}

for i in range(N):
    li[i] = int(input())

count = 0
for j in range(N-1,0,-1):
    if li[j] < li[j-1]:
        count += (li[j-1]) - li[j] + 1
        li[j-1] = li[j] - 1
    if li[j] == li[j-1]:
        count += 1
        li[j-1] -= 1

print(count)