# def twoSum(nums, target):
#     i = 0
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == target:
#                 return [i, j]
#     i += 1

# One pass solution __Dictionary
def twoSum(nums, target):
    dic = dict()
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dic.keys():
            return [dic[complement], i]
        dic[nums[i]] = i

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))