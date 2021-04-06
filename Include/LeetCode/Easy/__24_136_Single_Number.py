
def singleNumber(nums: list[int]) -> int:
    dic_num = dict()

    for i in range(len(nums)):
        if nums[i] not in dic_num:
            dic_num[nums[i]] = 1
        else:
            dic_num[nums[i]] += 1


    return min(dic_num, key=dic_num.get)


# def singleNumber(nums: list[int]) -> int:
#     a = 0
#     for i in nums:
#         a ^= i
#     return a

if __name__ == '__main__':
    nums = [2, 2, 1]
    res = singleNumber(nums)
    print(res)
