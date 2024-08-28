import sys
input = sys.stdin.readline

di = {}
while True:
    N = str(input().strip())

    if N == '':
        break
    else:
        if N in di:
            di[N] += 1
        else:
            di[N] = 1

sdic = sorted(di.items())
summ = sum(di.values())
for val in sdic:
    print(val[0], '%.4f' % (val[1] / summ * 100))
