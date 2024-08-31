N = int(input())
liquid = list(map(int, input().split()))

slid = sorted(liquid)

# 투포인터문제
left = 0
right = N - 1
best_sum = float('inf')
best_pair = (slid[left], slid[right])

while left < right:
    current_sum = slid[left] + slid[right]
    # 현재 합이 0에 더 가까운 경우 갱신
    if abs(current_sum) < abs(best_sum):
        best_sum = current_sum
        best_pair = (slid[left], slid[right])
    # 합이 0보다 크다면, right를 줄여 더 작은 값으로
    if current_sum > 0:
        right -= 1
    # 합이 0보다 작다면, left를 증가시켜 더 큰 값으로
    elif current_sum < 0:
        left += 1
    else:
        break

print(best_pair[0], best_pair[1])
