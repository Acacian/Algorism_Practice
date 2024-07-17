import sys
input = sys.stdin.readline

#x,y 값 입력받을 변수
cal = input().split()
x = int(cal[0]) - 1
y = int(cal[1])

# 전체 아이디어
# x * 31 + y * 1 / 1월부터 + 30하면 안되서 - 1함
#정확히 월요일마다 다음 달이 되는 게 아니기에 달 바뀐다고 초기화되면 안됨
#1년의 날은 한정되어 있으니까 이걸 나누기 7 해서 해결할거임
#특정 달에는 날짜가 달라진다는걸 인지하고, 해당 달이 있다면 따로 빼 줘야 함
# ((x * 31) + y) % 7 << 1달이 31일로 가정하고 전체 날짜 구하는 방식

# x를 그대로 넣는 이유는 예를 들어 3월달이 되어야 2월에 -3일 된 영향을 받기 때문
# 당연히 달에다 +1 해도 되지만 가독성을 위해 그냥 x를 조절하기로 결정
# 전체 날짜를 계산하기 위해 year 변수 생성
# 4 6 9 11 : 30 / 2 : 28
year = ((x * 31) + y)
if (x) >= 2 and (x) < 4:
    year -= 3
elif (x) >= 4 and (x) < 6:
    year -= 4
elif (x) >= 6 and (x) < 9:
    year -= 5
elif (x) >= 9 and (x) < 11:
    year -= 6
elif (x) >= 11:
    year -= 7


if year % 7 == 0:
    print("SUN")
elif year % 7 == 1:
    print("MON")
elif year % 7 == 2:
    print("TUE")
elif year % 7 == 3:
    print("WED")
elif year % 7 == 4:
    print("THU")
elif year % 7 == 5:
    print("FRI")
elif year % 7 == 6:
    print("SAT")
else:
    print("Calander Error")



