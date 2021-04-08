def diagonalDifference(arr):
    right = 0
    left = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                right += arr[i][j]
            if i + j == len(arr) - 1:
                left += arr[i][j]
    return abs(right - left)


if __name__ == '__main__':
    arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
    print(diagonalDifference(arr))