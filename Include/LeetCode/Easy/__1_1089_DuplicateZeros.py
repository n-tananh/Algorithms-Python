a = list(map(int, input().split()))

i = 0
while i < len(a) - 1:
    if a[i] == 0:
        for j in range(len(a) - 1, i, -1):
            a[j] = a[j - 1]
        a[i + 1] = 0
        i += 1
    i += 1

print(a)

