def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        mid = int((l + r) / 2)
        if nums[mid] > target:
            r = mid - 1
        elif nums[mid] < target:
            l = mid + 1
        else:
            return mid
    return -1


def biSearch(nums, left, right, target):

    if left > right:
        return -1
    middle = int((left + right) / 2)

    if target == nums[middle]:
        return middle
    if target > nums[middle]:
        return biSearch(nums, middle + 1, right, target)
    return biSearch(nums, left, middle - 1, target)

if __name__ == '__main__':
    nums = [5]
    target = 5
    print(search(nums, target))