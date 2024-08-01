# 단순 구현 문제

def switch():
    N = int(input())
    li = list(map(int, input().split()))
    studentsum = int(input())
    for _ in range(studentsum):
        student = list(map(int, input().split()))
        sex , sw = student[0], student[1]
        if sex == 1: #남자면 자기 스위치의 배수를 바꿈
            for i in range(N):
                if i % sw == sw - 1:
                    if li[i] == 0:
                        li[i] = 1
                    else:
                        li[i] = 0
                else:
                    continue
        else: # 여자면 양 옆 비교 후 같으면 다 바꾸고, 다르면 자기 숫자만 바꾼다.
            i = 1
            if (sw - 1 - i) >= 0 and (sw - 1 + i) <= N-1 and li[sw - 1 - i] != li[sw - 1 + i]:
                if li[sw - 1] == 0:
                    li[sw - 1] = 1
                else:
                    li[sw - 1] = 0
            else: # 만약 양 옆이 다르다면..
                if li[sw - 1] == 0:
                    li[sw - 1] = 1
                else:
                    li[sw - 1] = 0
                while (sw - 1 - i) >= 0 and (sw - 1 + i) <= N-1 and li[sw - 1 - i] == li[sw - 1 + i]:
                    if li[sw - 1 - i] == 0:
                        li[sw - 1 - i] = 1
                        li[sw - 1 + i] = 1
                    else:
                        li[sw - 1 - i] = 0
                        li[sw - 1 + i] = 0  
                    i += 1
    # 스위치 개수 파악
    for i in range(1,N+1):
        print(li[i-1], end=" ")
        if i % 20 == 0:
            print()

switch()