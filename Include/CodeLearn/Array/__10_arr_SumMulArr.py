m = int(input())
n = int(input())

matrix = []
for i in range(0,m):
    matrix.append([])
    for j in range(0,n):
        matrix[i].append(int(input()))

sum = 0
for i in range(0,m):
    for j in range(0,n):
        sum += matrix[i][j]

print(sum)