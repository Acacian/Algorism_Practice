from collections import deque

N = int(input())
a = input()
b = input()
A = deque(a)
B = deque(b)

# 그냥 어떻게 해도 브루트포스밖에 생각이 안나는데..?
# deque에서 빼면서 확인하면 될듯
# 맨 처음이랑 맨 끝 확인
# aeiou 다 빼고 비교했을 때 같아야 함
def check():
    if a[0] != b[0] or a[-1] != b[-1]:
        return "NO"
    
    # 재조합이 가능한지 확인해야함
    # sort 시켰을 때 같은지 아닌지 확인하면 됨
    if sorted(a) != sorted(b):
        return "NO"

    for _ in range(N):
        ebt , ebt2 = A.pop(), B.pop()
        if ebt not in ["a","e","i","o","u"]:
            A.appendleft(ebt)
        if ebt2 not in ["a","e","i","o","u"]:
            B.appendleft(ebt2)
    if A == B:
        return "YES"
    else:
        return "NO"
        
print(check())