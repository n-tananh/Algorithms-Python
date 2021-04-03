



def merge(nums1, nums2, m, n):
    m -= 1
    n -= 1

    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[m + n + 1] = nums1[m]
            m -= 1
        else:
            nums1[m + n + 1] = nums2[n]
            n -= 1
    if n >= 0:
        nums1[:n + 1] = nums2[:n + 1]

    return nums1

if __name__ == '__main__':
    nums1 = [11, 12, 0, 0, 0, 0, 0, 0]
    m = 2
    nums2 = [1, 2, 4, 6, 8, 10]
    n = 6


    print(merge(nums1, nums2, m, n))
