matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]

m = 3
n = 3



# chạy từ [1][1] cộng lên
# ví dụ
# 2 1 3
# 6 5 4
# 7 8 9
#
# chạy từ 5 cộng với min(matrix[0]) tức là min của (5 +1, 5 + 2, 5 + 3) gán giá trị mới ở 5 == 6
# tương tự với các th còn lại

for i in range(1, len(matrix)):
    for j in range(len(matrix[0])):
        if j == 0:
            matrix[i][j] += min(matrix[i - 1][j], matrix[i - 1][j + 1])
        elif j == len(matrix[0]) -1:
            matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j])
        else:
            matrix[i][j] += min(matrix[i - 1][j - 1], matrix[i - 1][j], matrix[i - 1][j + 1])

print(min(matrix[-1]))


