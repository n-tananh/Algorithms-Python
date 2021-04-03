# đầu tiên tạo 1 map để lưu trữ toàn bộ phần tử trong matrix với giá trị 0
# tìm kiếm phần tử nhỏ nhất trong từng hàng ---> tăng giá trị key trong map lên
# tìm kiếm phần tử lớn nhật trong từng cột --> tăng giá trị key trong map lên
# khi 1 số thoả mãn vừa lớn nhất trong cột và nhỏ nhất trong hàng thì sẽ có value trong map = 2

def luckyNumbers_solu(matrix):
    minrow = {min(r) for r in matrix}
    maxcol = {max(c) for c in zip(*matrix)}
    return list(minrow & maxcol)

def luckyNumbers (matrix):
    map = {}
    res = []
    for i in matrix:
        for j in i:
            map[j] = 0

    m = len(matrix)
    n = len(matrix[0])
    for i in range(0, m):
        minRow = matrix[i][0]
        for j in range(1, n):
            if minRow > matrix[i][j]:
                minRow = matrix[i][j]
        map[minRow] += 1

    for i in range(0, n):
        maxCol = matrix[0][i]
        for j in range(1, m):
            if maxCol < matrix[j][i]:
                maxCol = matrix[j][i]
        map[maxCol] += 1

    for key in map:
        if map[key] == 2:
            res.append(key)
    return res



if __name__ == '__main__':
    matrix = [[3, 7, 8], [9, 11, 13], [15, 16, 17]]

    matrix1 = [[1, 10, 4, 2], [9, 3, 8, 7], [15, 16, 17, 12]]

    matrix2 = [[7, 8], [1, 2]]

    luckyNumbers(matrix)