import sys
input = sys.stdin.readline

N = int(input())
users = set() # key/value 말고 중복만 탐지하는 set활용
count = 0

for _ in range(N):
    action = input().strip()
    
    if action == "ENTER":
        users.clear()
    elif action not in users:
        users.add(action)
        count += 1

print(count)