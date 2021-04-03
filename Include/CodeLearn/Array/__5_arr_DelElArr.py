n = int(input())
arr = []
for i in range(n):
    arr.append(input())
k = int(input())

for i in range(k , n-1):
    arr[i] = arr[i+1]
arr.pop(n-1)
print(arr)


