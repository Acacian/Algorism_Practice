import sys
input = sys.stdin.readline
threedice = input().split()
# 3 5 5 > ['3' '5' '5']

# 1,2 / 1,3 번째가 같을 수 있고, 2,3번째가 같을 수 있다. 
# 3개밖에 없으니까 for문으로 bruteforce 하면서 동일여부 파악
# 만약 2개만 같으면 + 1000, 3개 다 같으면 + 10000
# 같은 게 없다면 가장 큰 수 

# 같은 숫자 or 가장 큰 숫자를 저장해 놓을 상수 하나 지정
num = 0
# 같은 숫자 수를 카운트할 숫자 하나 지정
count = 0
for i in range(1,3):
    # 첫 번째 자리는 어짜피 이전 걸 보기 때문에 체크할 필요가 없음
    if threedice[i-1] == threedice[i]:
        # 양 옆 숫자를 비교해서, 같다면 카운트에 추가하고 num을 맞춰 줌
        count += 1
        num = int(threedice[i])
    # 만약 첫 번째, 세 번째 주사위의 수만 같은 경우
    elif i == 2 and threedice[i-2] == threedice[i] and count == 0:
        count += 1
        num = int(threedice[i])
    # 셋 다 다른 경우
    elif i == 2 and threedice[i-2] != threedice[i-1] and threedice[i-1] != threedice[i]:
        num = max(int(threedice[i]), int(threedice[i-1]), int(threedice[i-2]))

# 돈 저장할 변수
money = 0
if count == 2:
    money = 10000 + (num * 1000)
elif count == 1:
    money = 1000 + (num * 100)
else:
    money = num * 100

print(money)