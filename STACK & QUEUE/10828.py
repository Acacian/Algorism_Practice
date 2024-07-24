# from collections import deque
# 생각해봤는데 스텍이라 [ ] 로도 해결됨

N = int(input())
li = []
for _ in range(N):
    li.append(input().split())

# 답변을 받을 새로운 스텍
st = []
for i in range(N):
    if len(li[i]) == 2: # push면
        st.append(li[i][1])
    else:
        if li[i] == ['top'] and len(st) == 0:
            print(-1)
        elif li[i] == ['top'] and len(st) > 0:
            print(st[-1])
        elif li[i] == ['empty'] and len(st) == 0:
            print(1)
        elif li[i] == ['empty'] and len(st) > 0:
            print(0)     
        elif li[i] == ['size']:
            print(len(st))  
        elif li[i] == ['pop'] and len(st) == 0:
            print(-1)
        elif li[i] == ['pop'] and len(st) > 0:
            print(st.pop())