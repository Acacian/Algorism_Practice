import sys
input = sys.stdin.readline

N = int(input())
users = set()  # 현재 채팅방에 있는 사용자를 추적
count = 0  # 곰곰티콘 사용 횟수

for _ in range(N):
    action = input().strip()
    
    if action == "ENTER":
        users.clear()  # 새 사람이 들어오면 사용자 집합을 초기화
    elif action not in users:
        users.add(action)  # 새로운 사용자가 채팅을 치면 집합에 추가
        count += 1  # 곰곰티콘 사용 횟수 증가

print(count)