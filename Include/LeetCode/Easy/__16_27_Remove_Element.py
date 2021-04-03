def removeElement(nums, val):
    if len(nums) == 0:
        return 0

    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count += 1

    return count

if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3

    print(removeElement(nums, val))
