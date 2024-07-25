import sys
input = sys.stdin.readline

N = int(input())
Gift = []

def push(x):
    for k in range(1, len(x)):
        Gift.append(x[k])
        i = len(Gift) - 1
        while i > 0 and Gift[(i-1)//2] < Gift[i]:
            Gift[(i-1)//2], Gift[i] = Gift[i], Gift[(i-1)//2]
            i = (i-1)//2

def pop():
    if not Gift:
        return -1
    if len(Gift) == 1:
        return Gift.pop()
    
    result = Gift[0]
    Gift[0] = Gift.pop()
    i = 0
    while i * 2 + 1 < len(Gift):
        child = i * 2 + 1
        if child + 1 < len(Gift) and Gift[child] < Gift[child + 1]:
            child += 1
        if Gift[i] >= Gift[child]:
            break
        Gift[i], Gift[child] = Gift[child], Gift[i]
        i = child
    return result

for _ in range(N):
    x = list(map(int, input().split()))
    if x == [0]:
        print(pop())
    else:
        push(x)