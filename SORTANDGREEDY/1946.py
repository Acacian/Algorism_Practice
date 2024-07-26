import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    M = int(input())
    applicants = []
    for _ in range(M):
        a, b = map(int, input().split())
        applicants.append((a, b))
    
    # 서류 성적(a)을 기준으로 정렬
    applicants.sort()  # 튜플의 첫 번째 요소를 기준으로 자동 정렬됩니다.
    
    count = 1  # 서류 1등은 무조건 선발
    hst2 = applicants[0][1]  # 현재까지의 최고 면접 순위
    
    for i in range(1, M):
        if applicants[i][1] < hst2:
            count += 1
            hst2 = applicants[i][1]
    
    print(count)