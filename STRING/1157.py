import sys
input = sys.stdin.readline

word = list(map(str,input()))

# 전체 대문자로 만들어서 카운트하기 쉽게
words = []
for i in range(len(word)-1):
    words.append(word[i].upper())

# 정렬해서 앞뒤 다르면 다른 알파벳으로 구분
words.sort()

count = 0
max = 0
alphabet = ''
# 브루트포스
# 1부터 시작하는 이유는 /n 무시하고 시작하기 위해서
t = len(words)

if len(words)-1 == 0:
    print(*words)
else:
    for i in range(len(words)-1):
        if words[i] == words[i+1]:
            count += 1
            if count == max:
                alphabet = "?"
            elif count > max:
                alphabet = words[i]
                max = count
        else:
            count = 0
    # 모든 알파벳이 다 한글자씩 있음
    if count == 0 and max == 0:
        alphabet = "?"

print(alphabet)