n = int(input())
li = dict()
for _ in range(n):
    sr = input().split(".")
    if sr[1] in li:
        li[sr[1]] += 1
    else:
        li[sr[1]] = 1

li = dict(sorted(li.items()))

for ext, count in li.items():
    print("{} {}".format(ext, count))