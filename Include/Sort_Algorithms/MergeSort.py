def merge(a1, a2):
    n = len(a1) + len(a2)
    res = [0] * n

    i = 0
    i1 = 0
    i2 = 0
    while i < n:
        if i1 < len(a1) and i2 < len(a2):
            if a1[i1] <= a2[i2]:
                res[i] = a1[i1]
                i += 1
                i1 += 1
            else:
                res[i] = a2[i2]
                i += 1
                i2 += 1
        else:
            if i1 < len(a1):  # a1 oke
                res[i] = a1[i1]
                i += 1
                i1 += 1
            else:  # a2 oke
                res[i] = a2[i2]
                i += 1
                i2 += 1

    return res

def mergeSort(nums, left, right):
    if left > right:
        return [0]
    if left == right:
        singleElement = [nums[left]]
        return singleElement

    # Chia ra
    print("Chia ra " + str(left) + " - " + str(right))
    mid = left + (right - left) // 2
    a1 = mergeSort(nums, left, mid)
    a2 = mergeSort(nums, mid + 1, right)

    res = merge(a1, a2)
    print("Ket qua merge: ", res)
    return res


if __name__ == '__main__':
    nums = [1, 5, 3, 2, 8, 7, 6, 4]
    a = [1, 3, 5, 7, 9]
    b = [2, 4, 6, 8, 10]

    print(mergeSort(nums, 0, len(nums) - 1))
