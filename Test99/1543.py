N = input() # 긴거
M = input() # 짧은거

def checking():
    count = 0
    # M의 첫 문자가 N의 어디에서부터 시작함?
    save_point = 0 # 중복된 곳에서부턴 시작 불가
    for i in range(len(N) - len(M) + 1):
        if i >= save_point and N[i] == M[0]:
            for j in range(len(M)):
                a = N[i+j]
                b = M[j]
                c = len(M)
                if a != b:
                    break # 안 똑같음
                if j == c-1:
                    save_point = i+j+1
                    count += 1
    return count

print(checking())