def getRow(rowIndex):
    ans = [0] * (rowIndex + 1)
    ans[0] = 1
    for i in range(1, rowIndex  +1):
        for j in range(i, 0, -1):
            ans[j] += ans[j-1]
    return ans

if __name__ == '__main__':
    rowIdx = int(input())
    print(getRow(rowIdx))