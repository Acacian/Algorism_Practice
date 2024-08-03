N = int(input())

def mincoin(x):
    count = 0
    val = [5,2] # 동전
    if x == 1 or x == 3:
        return -1

    for value in val:
        if x == 0: #끝나는 조건
            break
        count += x // value
        x %= value

        if value == 5 and x % 2 == 1:
            count -= 1
            x += 5

        if value == 2 and x % 2 == 1:
            return -1
    
    return count

print(mincoin(N))