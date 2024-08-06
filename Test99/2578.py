arr = []
for i in range(5):
    arr.append(list(map(int,input().split())))
checklist = []
for i in range(5):
    checklist.extend(list(map(int,input().split())))

def bingo():
    # 체크
    for i in range(25):
        count = 0
        if arr[0][0] == arr[1][1] == arr[2][2] == arr[3][3] == arr[4][4]:
                count += 1
        if arr[0][4] == arr[1][3] == arr[2][2] == arr[3][1] == arr[4][0]:
                count += 1
        for o in range(5):
            if arr[o][0] == arr[o][1] == arr[o][2] == arr[o][3] == arr[o][4]:
                count += 1
            if arr[0][o] == arr[1][o] == arr[2][o] == arr[3][o] == arr[4][o]:
                count += 1

        if count >= 3:
            return i

        c = checklist[i]
        for j in range(5):
            for k in range(5):
                a = arr[j][k]
                if c == a:
                    arr[j][k] = "X"
                        
    # 빙고가 없는게 말이안됨. 예외처리
    return -1
print(bingo())