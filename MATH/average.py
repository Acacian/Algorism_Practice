import sys
input = sys.stdin.readline
C = int(input())
li = []
# 학생들은 반이 있기 때문에 리스트로 표현한다. C 번 받아야 하니 for문으로 순회하면서 정리한다.
for _ in range(C):
    li.append(list(map(int, input().split())))

# for문으로 list 내를 순회하면서 평균값을 낸다. 단, 결과는 float로 받아야 한다.
# 첫 자리는 학생 수이므로 따로 변수를 순회해서 받는다.
# 전체 학생 점수를 계산할 변수를 만든다.
num = 0
for i in range(C):
    num = li[i][0]
    # 다시 순회하기 위해 초기화해준다.
    tot = 0
    avg = 0
    ps = 0
    # 첫 자리를 빼고 그 뒤부터 학생들의 성적을 조회한다.
    for j in range(1, num+1):
        tot = tot + li[i][j]
    avg = tot/num
    # 학생들의 평균 여부를 조회한다.
    for k in range(1, num+1):
        if li[i][k] > avg:
            ps += 1

    # 백분율은 도저히 기억이 안 나서 인터넷 참고했습니다.
    print('{:.3%}'.format(ps / num))