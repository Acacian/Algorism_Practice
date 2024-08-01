N = int(input())

students = [list(map(int, input().split())) for _ in range(N)]

# 각 학생별로 같은 반이었던 학생 수를 저장할 리스트
same_class_count = [0] * N

for i in range(N):
    for j in range(i+1, N):  # 자기 자신과는 비교할 필요 없음
        if any(students[i][year] == students[j][year] for year in range(5)):
            same_class_count[i] += 1
            same_class_count[j] += 1

# 가장 많은 학생과 같은 반이었던 학생 번호 찾기 (번호는 1부터 시작)
print(same_class_count.index(max(same_class_count)) + 1)

# N = int(input())

# li = []
# for _ in range(N):
#     li.append(list(map(int,input().split())))

# counter = [[0 for _ in range(N)] for _ in range(N)]
# for i in range(N):
#     for j in range(N-1):
#         for k in range(j+1,N):
#             if j < N-1 and li[j][i] == li[k][i]:
#                 if counter[j][i] == 0:
#                     counter[j][i] += 1
#                 if counter[k][i] == 0:
#                     counter[k][i] += 1
#                 break

# counter2 = [[0,0] for _ in range(N)]
# for i in range(N):
#     counter2[i][0] = i+1
#     for j in range(N):
#         if counter[i][j] == 1:
#             counter2[i][1] += 1
# counter2.sort(key= lambda x : x[1] , reverse=True)

# print(counter2[0][0])