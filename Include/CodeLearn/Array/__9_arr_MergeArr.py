n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

c = []
i , j = 0, 0
while i < n and j < m:
    if a[i] >= b[j]:
        c.append(b[j])
        j += 1
    else:
        c.append(a[i])
        i += 1
while i < n:
    c.append(a[i])
    i += 1

while j < m:
    c.append(b[j])
    j += 1

for i in c:
    print(i, end= " ")