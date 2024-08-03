from collections import deque

def cardgame():
    num = int(input())
    cards = deque(list(map(str,input().split())))
    field = deque()
    
    while cards:
        dc = cards.popleft()
        if len(field) == 0:
            # 필드가 비어 있다면, 그냥 놔둔다
            field.append(dc)
        else:
            # 필드가 있다면, 필드 맨 앞과 비교한다.
            check = field.popleft()
            compare = [dc,check]
            compare.sort()

            if compare[0] == dc: #뽑았던 게 더 빠름
                field.appendleft(check)
                field.appendleft(dc)
            else:
                field.appendleft(check)
                field.append(dc)

    print(*field , sep="")

N = int(input())
for _ in range(N):
    cardgame()