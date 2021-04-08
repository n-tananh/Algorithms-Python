def compareTriplets(a, b):
    res = [0, 0]
    for i in range(3):
        if a[i] > b[i]:
            res[0] += 1
        elif a[i] < b[i]:
            res[1] += 1
        else:
            continue
    return res
if __name__ == '__main__':
    a = [17, 28, 30]
    b = [99, 16, 8]
    print(compareTriplets(a, b))