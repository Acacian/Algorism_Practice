from collections import deque
import sys

input = sys.stdin.readline

left = deque(input().strip())
right = deque()

# 하나의 리스트만 사용하면 중간에 못 넣으니까 저장용으로 하나 더 만듬
for _ in range(int(input())):
    word = input().strip()
    
    if word == 'L':
        if left:
            right.appendleft(left.pop())
    elif word == 'D':
        if right:
            left.append(right.popleft())
    elif word == 'B':
        if left:
            left.pop()
    elif word.startswith('P'):
        left.append(word[2])

print(''.join(left) + ''.join(right))

# word = list(input())
# li = []
# N = int(input())
# for _ in range(N):
#     li.append(input().split())

# # 맨 끝 자리가 어디인지 확인하기 위한 용도
# lw = len(word)
# for i in range(N):
#     if len(li[i]) == 2:
#         word.insert(lw, li[i][1])
#         lw += 1

#     else:
#         if li[i] == ['L']:
#             if lw > 0:
#                 lw -= 1
#         if li[i] == ['D']:
#             if lw < len(word):
#                 lw += 1
#         if li[i] == ['B']:
#             if lw-1 >= 0:
#                 word.pop(lw-1)
#                 lw -= 1
#             else:
#                 continue

# print(''.join(word))