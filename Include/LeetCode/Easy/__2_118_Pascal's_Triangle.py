h =  int(input())

matrix = []
for i in range(0, h):
    matrix.append([])
    for j in range(i + 1):
        matrix[i].append(0)



for i in range(len(matrix)):
    # vòng ngoài cũng cảu tam giác sẽ có giá trị bằng 1
    matrix[i][0] = matrix[i][i] = 1

    # quá trình cộng dồn theo công thức của tam giád pascal
    for k in range(2, len(matrix)): #cho k chạy từ 2 vì bắt đầu từ 2 mới fill
        for l in range(1, k):
            matrix[k][l] = matrix[k - 1][l - 1] + matrix[k - 1][l]


print(matrix)

j = int(input())

print(matrix[j - 1])