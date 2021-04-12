def threeSum(nums: list[int]) -> list[list[int]]:
    res = []
    nums.sort()
    for i in range(len(nums) - 2):
        if nums[i] < 0:
            if i == 0 or (i > 0 and (nums[i] != nums[i - 1])):
                low = i + 1
                high = len(nums) - 1
                sum_tmp = 0 - nums[i]
                while low < high:
                    if nums[low] + nums[high] == sum_tmp:
                        res.append([nums[i], nums[low], nums[high]])
                        while low < high and nums[low] == nums[low + 1]:
                            low += 1
                        while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif nums[low] + nums[high] < sum_tmp:
                        low += 1
                    else:
                        high -= 1

    return res


if __name__ == '__main__':
    nums = [0, 0, 1, 2, 1, 4]

    print(threeSum(nums))
