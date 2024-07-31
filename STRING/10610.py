def solution():
    N = input().strip()
    digits = list(map(int, N))
    
    if '0' not in N:
        return -1
    
    if sum(digits) % 3 != 0:
        return -1
    
    digits.sort(reverse=True)
    
    return int(''.join(map(str, digits)))

print(solution())