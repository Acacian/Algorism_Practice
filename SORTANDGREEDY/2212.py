# 문제 이해가 더 어려운 문제
N = int(input()) # 센서 수
M = int(input()) # 집중국 수
li = list(map(int,input().split()))
li.sort()

# 서로간의 거리를 구하자
load = []
for i in range(1,N):
    load.append(abs(li[i] - li[i-1]))
load.sort()

count = 0
for j in range(len(load) - (M-1)):
    count += load[j]

print(count)