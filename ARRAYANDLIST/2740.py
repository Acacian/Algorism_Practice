import sys
input = sys.stdin.readline

NM = list(map(int, input().split()))
N = NM[0]
M = NM[1]
li = []
for _ in range(N):
    li.append(list(map(int, input().split())))

MK = list(map(int, input().split()))
K = MK[1]
li2 = []
for _ in range(M):
    li2.append(list(map(int, input().split())))

# 하나는 가로로 늘어나고, 하나는 세로로 늘어나서 이들의 곱들을 합해야 함
# M 은 중복됨. 즉 무조건 대칭된다는 말 / ex) 3*2 2*3(2 중복)
for i in range(N):
    ans = []
    # 여기까지 해서 맨 위의 배열을 가져옴
    for k in range(K):
        tot = 0
        for j in range(M):
            # 행렬 곱 : 맨 처음 행렬의 첫 번째 <<= 다른 행렬의 첫/두/세번째가 대칭
            lef = li[i][j]
            rig = li2[j][k]
            tot += lef * rig
        ans.append(tot)
    print(*ans)










