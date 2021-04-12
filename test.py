def twoSum(nums: list[int], target: int) -> list[int]:

    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


if __name__ == '__main__':
    nums = [0, 3, 2, 7]
    target = 9
    print(twoSum(nums, target))