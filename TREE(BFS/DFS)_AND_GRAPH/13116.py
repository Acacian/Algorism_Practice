N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    while(True):
        if(a>b):
            a //= 2
        elif(a<b):
            b //= 2
        elif(a==b):
            print(a*10)
            break