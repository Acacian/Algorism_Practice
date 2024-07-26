N = int(input())
arr = []
for i in range(N):
    arr.append(str(input()))

arr.sort(key= lambda x : (len(x), x))

for i in range(len(arr)):
    print(arr[i])
