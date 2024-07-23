# 문제가 어렵다기보단 인덱스 에러 때문에 개고생한 문제

N = int(input())
li = list(map(int, input().split()))
studentsum = int(input())

# 사실 queue 를 import해서 fifo 방식으로 풀까도 생각했는데 귀찮음
for _ in range(studentsum):
    # 성별 / 스위치 개수로 나눔
    sex, switch = map(int, input().split())

    if sex == 1: # 남자아이 : 나눴을 때 나머지가 0이면 스위치 바꿈
        for i in range(1,len(li)+1):
            if i % switch == 0:
                if li[i-1] == 0:
                    li[i-1] = 1
                else:
                    li[i-1] = 0
    else: # 여자아이 : 좌우 인덱스 비교해서 다를 때까지 (자기 포함해서 << 이거 몰라서 헛고생) 좌우 다 바꾸고, 다르면 자기만 바꿈
        #인덱스 번호 맞춰줌
        switch -= 1

        if li[switch] == 1:
            li[switch] = 0
        else:
            li[switch] = 1

        for i in range(1,len(li)):
            if switch - i < 0 or switch + i > len(li) - 1:
                break
            if li[switch-i] == li[switch+i]:
                if li[switch-i] == 0 and li[switch+i] == 0:
                    li[switch-i] = 1
                    li[switch+i] = 1
                elif li[switch-i] == 1 and li[switch+i] == 1:
                    li[switch-i] = 0
                    li[switch+i] = 0
                else:
                    break
            else:
                break

# 20개마다 줄바꿈해야함
for i in range(1,N+1):
    print(li[i-1], end=" ")
    if i % 20 == 0:
        print()