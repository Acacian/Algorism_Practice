li = []
for _ in range(19):
    li.append(list(map(int,input().split())))

# 기본적으로 승부가 결정되지 않았다고 가정
ans = 0

# 좌우상하대각찾기
# 재귀로 풀려다가 잘 안되서 바꿈
count = 0
for i in range(1,20):
    for j in range(1,20):
        for k in range(5):
            if li[i][j] == li[i][j+k]:
                count += 1
            else:
                count = 0

            if li[i][j] == li[i+k][j]:
                count += 1
            else:
                count = 0

            if li[i][j] == li[i+k][j+k]:
                count += 1
            else:
                count = 0
