import sys
input = sys.stdin.readline

NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
K = int(input())
li = []
for _ in range(K):
    li.append(list(map(int, input().split())))

# 첫 리스트에서 요소를 가져오는방법
# arr[li[0][0] - 1][li[0][1] - 1] , arr[li[0][2] - 1][li[0][3] - 1]
for i in range(K):
    # print(arr[li[i][0] - 1][li[i][1] - 1] , arr[li[i][2] - 1][li[i][3] - 1])
    #세로
    count = 0
    for j in range(li[i][0] - 1 , li[i][2]):
        #가로
        for k in range(li[i][1] - 1 , li[i][3]):
            count += arr[j][k]
    print(count)

