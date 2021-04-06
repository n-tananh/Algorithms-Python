# def findDisappearedNumbers(nums: list[int]) -> list[int]:
#     # res = [i for i in range(1, len(nums) + 1) if i not in nums]
#
#     # Dùng màng đánh dấu
#     res = []
#     marked = [False] * len(nums)
#     for i in range(len(nums)):
#         index = abs(nums[i])
#         if marked[index - 1] is False:
#             marked[index - 1] = True
#
#     for i in range(len(marked)):
#         if marked[i] is False:
#             res.append(i + 1)
#
#     return res

# res = [i for i in range(1, len(nums) + 1) if i not in nums]
# def findDisappearedNumbers(nums: list[int]) -> list[int]:
#
#     # Không dùng mảng đánh dấu, chỉnh sửa ngay tại mảng ban đầu
#     res = []
#     for i in range(len(nums)):
#         index = abs(nums[i])
#         if nums[index - 1] > 0:
#             nums[index - 1] *= -1
#
#     for i in range(len(nums)):
#         if nums[i] > 0:
#             res.append(i + 1)
#
#     return res


"""Dùng cách dổi chổ phần tư
    nums = [4, 3, 2, 7, 8, 2, 3, 1]

    sau khi chạy đổi chỗ, những số sẽ về đúng vị trí,
     đến cuối những sô thiếu sẽ có thể thấy
    [7, 3, 2, 4, 8, 2, 3, 1]
    [3, 3, 2, 4, 8, 2, 7, 1]
    [2, 3, 3, 4, 8, 2, 7, 1]
    [3, 2, 3, 4, 8, 2, 7, 1]
    [3, 2, 3, 4, 1, 2, 7, 8]
--> [1, 2, 3, 4, 3, 2, 7, 8]
"""
def findDisappearedNumbers(nums: list[int]) -> list[int]:

    # Không dùng mảng đánh dấu, chỉnh sửa ngay tại mảng ban đầu
    # res = []
    # for i in range(len(nums)):
    #     index = abs(nums[i])
    #     if nums[index - 1] > 0:
    #         nums[index - 1] *= -1
    #
    # for i in range(len(nums)):
    #     if nums[i] > 0:
    #         res.append(i + 1)
    #
    # return res
    res = []
    for i in range(len(nums)):
        while nums[i] != (i + 1) and nums[i] != (nums[nums[i] - 1]):
            tmp = nums[i]
            nums[i] = nums[tmp - 1]
            nums[tmp - 1] = tmp
            print(nums)

    for i in range(len(nums)):
        if nums[i] != i + 1:
            res.append(i + 1)

    return res

if __name__ == '__main__':
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(findDisappearedNumbers(nums))