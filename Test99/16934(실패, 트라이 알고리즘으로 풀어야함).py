li = {}
N = int(input())
for _ in range(N):
    s = input()
    # 쪼개서 다 담아보면
    word = str()
    wordlist = []
    for i in range(len(s)):
        word = word + s[i]

        if word in li.keys():
            continue
        else:
            wordlist.append(word)
            li[word] = 0

    if len(wordlist) == 0 and li[s] != 0: # 같은 단어 중복
        wordlist.append(s+str(li[s]+1))
        li[s] += 1
    else:
        if len(wordlist) == 0:
            wordlist.append(s)
        if li[min(wordlist)] == 0:
            li[min(wordlist)] = 1

    print(min(wordlist))