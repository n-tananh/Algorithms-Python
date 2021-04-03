# def moveZeroes(nums):
#     """
#     :type nums: List[int]
#     :rtype: None Do not return anything, modify nums in-place instead.
#     """
#     ''' Input: nums = [0,1,0,3,12]
#         Output: [1,3,12,0,0]        '''
#
#     if len(nums) < 1:
#         return nums
#
#
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             for j in range(i + 1, len(nums)):
#                 if nums[j] != 0:
#                     nums[i] = nums[j]
#                     nums[j] = 0
#                     break
#     return nums

def moveZeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            tmp = nums[left]
            nums[left] = nums[right]
            nums[right] = tmp
            left += 1

    return nums

if __name__ == '__main__':
    # nums = [1, 0]
    # nums = [0, 1, 0, 3, 12]

    nums = [0, 0, 1]

    print(moveZeroes(nums))
