def miniMaxSum(arr):
    arr.sort()
    sumA = sum(arr)
    minA = sumA - max(arr)
    maxA = sumA - min(arr)
    print(minA, " ", maxA)

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    miniMaxSum(arr)