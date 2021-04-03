
"""E:\Coding\Python\SEQAB.pdf"""

a = [7, 2, 5, 3]

b = [4, 6, 3, 8]
n = 4
# a = [6, 8, 9, 3]
# b = [5, 8, 2, 1]


minArr = []

tmp = []
for i in range(n - 1):
    for j in range(i + 1, n):
        tmp.append(a[i] + a[j])
        for k in range(i, j + 1):
            tmp.append(b[k])
        minArr.append(min(tmp))
        tmp.clear()

print(max(minArr))
