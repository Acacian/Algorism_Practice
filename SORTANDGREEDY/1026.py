import sys
input = sys.stdin.readline

N = int(input())
li1 = list(map(int, input().split()))
li2 = list(map(int, input().split()))

# li1에선 큰 숫자대로 정렬, li2에선 작은 숫자대로 정렬
li1.sort()
li2.sort(reverse=True)

count = 0
for i in range(N):
    count += li1[i] * li2[i]

print(count)