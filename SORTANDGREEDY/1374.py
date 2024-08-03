import heapq

N = int(input())

lectures = []
for _ in range(N):
    lecture_info = list(map(int, input().split()))
    start = lecture_info[1]
    end = lecture_info[2]
    lectures.append([start, end])

# 시작 시간 기준으로 정렬
lectures.sort(key=lambda x: x[0])

# 최소 힙 사용
min_heap = []
heapq.heappush(min_heap, lectures[0][1])  # 첫 강의의 종료 시간을 넣음

for i in range(1, N):
    # 가장 먼저 끝나는 강의가 현재 강의의 시작 시간보다 작거나 같으면 제거
    if min_heap[0] <= lectures[i][0]:
        heapq.heappop(min_heap)
    # 현재 강의의 종료 시간을 힙에 추가
    heapq.heappush(min_heap, lectures[i][1])

# 최소 강의실 개수는 힙의 크기
print(len(min_heap))
