n = int(input())
arr = list(map(int, input().split()))

inCrease = True
deCrease = True

for i in range(1, n):
        if arr[i] >= arr[i-1]: inCrease = False
        if arr[i] <= arr[i-1]: deCrease = False

if inCrease or deCrease:
    print("YES")
else:
    print("NO")



