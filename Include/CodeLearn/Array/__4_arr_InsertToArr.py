
n = int(input())
arr = [0] * (n+1)

for i in range(n):
    arr[i] = int(input())

k = int(input())
x = int(input())

for i in range(n,k,-1):
    arr[i] = arr[i+1]

arr[k] = x

for i in arr:
    print(i, end= " ")
