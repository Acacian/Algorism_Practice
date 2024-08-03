# daldidalgo / daldidan
# daldi 까지는 입력하고 / dal 은 앞에서 가져오고 / go는 본인이 입력
# N = 2일때, daldi(5) dal(1) go(2) daldidalgo(1) daldida(1) n(1)
# 총 11번

N = int(input())
count = 0
# 일단 앞의 daldidalgo에서 8번은 고정, daldidan에서 2번 고정임
count += 10
# 예를 들어 D(달디달고 줄임)를 5번 하게 되면, D > DD > DDDD > DDDDD가 되므로
# D > DD > DDD > DDDD > DDDDD와 다르게 횟수가 줄어듬 이게 관건인듯
# 2의 n 승 안에 있느냐 없느냐로 보면 될듯
if N == 1:
    print(count)
else:
    i = 1
    while 2 ** i <= N:
        count += 1
        i += 1
    print(count)

