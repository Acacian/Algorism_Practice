# 아래는 틀린 식임

# li = []
# for _ in range(19):
#     li.append(list(map(int,input().split())))

# # 기본적으로 승부가 결정되지 않았다고 가정
# ans = 0

# # 좌우상하대각찾기
# # 재귀로 풀려다가 시간 너무 오래 걸리고 잘 안되서 바꿈
# rowcount = 1
# colcount = 1
# zcount = 1
# for i in range(1,15):
#     for j in range(1,15):
#         if li[i][j] != 0:
#             for k in range(1,6):
#                 if rowcount > 5:
#                     rowcount = 1
#                     break
#                 if li[i][j] == li[i][j+k]:
#                     rowcount += 1
#                 elif li[i][j] != li[i][j+k] and rowcount == 5:
#                     print("있다")
#                 else:
#                     rowcount = 1
#                     break

#                 if colcount > 5:
#                     colcount = 1
#                     break
#                 if li[i][j] == li[i+k][j]:
#                     colcount += 1
#                 elif li[i][j] != li[i+k][j] and colcount == 5:
#                     print("있다")
#                 else:
#                     colcount = 1
#                     break

#                 if zcount > 5:
#                     zcount = 1
#                     break
#                 if li[i][j] == li[i+k][j+k]:
#                     zcount += 1
#                 elif li[i][j] != li[i+k][j+k] and zcount == 5:
#                     print("있다")
#                 else:
#                     zcount = 1
#                     break