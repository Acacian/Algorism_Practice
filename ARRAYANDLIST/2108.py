from collections import Counter

N = int(input())
li = []
for _ in range(N):
    li.append(int(input()))

# 산술평균
print(round(sum(li) / N))

# 중앙값
li.sort()
print(li[N//2])

# 최빈값
# set로 구해도 되긴한데.. 생각이 안나요
counter = Counter(li)
mode = counter.most_common()
if len(mode) > 1 and mode[0][1] == mode[1][1]:
    val = mode[1][0]
else:
    val = mode[0][0]
print(val)

# 범위
print(li[-1] - li[0])

