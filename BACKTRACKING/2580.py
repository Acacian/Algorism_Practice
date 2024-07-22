import sys
input = sys.stdin.readline

stoku = []
for i in range(9):
    stoku.append(list(map(int, input().split())))

def backtracking(depth):
    if depth == 81:
        for row in stoku:
            print(*row)
        return True

    y, x = depth // 9, depth % 9
    if stoku[y][x] != 0:
        return backtracking(depth + 1)

    for num in range(1, 10):
        # 행, 열, 3x3 박스 검사를 한 번에 수행
        if (num not in stoku[y] and # 현재 행에 같은 숫자 X
            num not in [stoku[i][x] for i in range(9)] and # 현재 열에 같은 숫자 X
            num not in [stoku[y//3*3+i][x//3*3+j] for i in range(3) for j in range(3)]):
            # 3x3 박스 내 같은 숫자 x
            
            stoku[y][x] = num
            if backtracking(depth + 1):
                return True
            stoku[y][x] = 0

    return False # 1~9까지 다 해봤는데 뭐 되는 게 없는 경우

backtracking(0)