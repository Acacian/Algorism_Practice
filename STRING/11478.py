n = str(input())

li = dict()

# 몇 번 배열을 반복할 것인가
for i in range(1,len(n)+1):
    # 하나씩 연결하는 수를 늘림
    for j in range(0,len(n)):
        if len(n[j:j+i]) >= i and n[j:j+i] in li:
            li[n[j:j+i]] += 1
        else:
            li[n[j:j+i]] = 0
            # li.append(n[j:j+i])

print(len(li))