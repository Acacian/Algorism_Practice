def ST():
    S = input()
    T = input()

    while len(T) > len(S):
        if T.endswith('A'):
            T = T[:-1]
        elif T.endswith('B'):
            T = T[:-1][::-1]
        else:
            return 0
    
    return 1 if S == T else 0

print(ST())

# # A 를 뒤에 넣거나, 뒤집고 B를 넣거나 둘 중 하나
# def ST():
#     S = input()
#     T = input()

#     if S == T:
#         return 1   
#     else:
#         # S 뒤와 T 위치를 비교
#         # 만약 A를 넣었는데 그게 T안에 없다면, 거꾸로 뒤집고 B를 투입 
#         while len(S) < len(T):
#             if (S + "A") in T:
#                 S = S + "A"
#             else:
#                 S = S[::-1] + "B"
#         if S == T:
#             return 1
#         else:
#             return 0

# print(ST())