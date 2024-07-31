# 어짜피 같은 수업을 듣진 않을거니 이름 필요없음
# dict 쓰면 학점별로 저장되서 빠를듯?

li = []
for _ in range(20):
    arr = list(map(str,input().split()))
    li.append([arr[1] , arr[2]]) # 학점, 등급

sum = 0
Asum = 0
for i in range(20):
    A = float(li[i][0])
    B = li[i][1]
    # 시간이 되면 더블 링크드 리스트로 찾아도 될 듯요..?
    if B == "A+":
        B = 4.5
    elif B == "A0":
        B = 4
    elif B == "B+":
        B = 3.5
    elif B == "B0":
        B = 3
    elif B == "C+":
        B = 2.5
    elif B == "C0":
        B = 2
    elif B == "D+":
        B = 1.5
    elif B == "D0":
        B = 1
    elif B == "F":
        B = 0
    elif B == "P":
        A = 0
        B = 0

    Asum += A
    sum += A * B

print(sum/Asum)
