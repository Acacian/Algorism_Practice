import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

# 원본 리스트의 값과 인덱스를 함께 저장
indexed_li = list(enumerate(li))

# 값을 기준으로 정렬
indexed_li.sort(key=lambda x: x[1])
print(indexed_li)

# 압축된 좌표를 저장할 딕셔너리
compressed = {}

# 현재 압축 값
current_compress = 0

for i, val in indexed_li:
    if val not in compressed:
        compressed[val] = current_compress
        current_compress += 1

print(li)
print(compressed)

# 결과 리스트 생성
result = [0] * N
for i, val in enumerate(li):
    result[i] = compressed[val]

print(*result)

# import sys
# input = sys.stdin.readline

# N = int(input())
# li = list(map(int, input().split()))
# # 인덱스 값 저장해놓기
# cpli = []
# ans = [0] * N
# for i in range(N):
#     cpli.append(li[i])
# li.sort()

# same = 0
# for j in range(N):
#     if li[j] == li[j-1]:
#         same += 1
#     else:
#         for k in range(N):
#             if li[j] == cpli[k]:
#                 ans[k] = j - same

# print(*ans)