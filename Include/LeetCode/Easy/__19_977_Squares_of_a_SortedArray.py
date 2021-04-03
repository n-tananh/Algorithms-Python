

def solution1(nums):
    left = -1
    while (left + 1 < len(nums)) and (nums[left + 1] < 0):
        left += 1

    right = len(nums)
    while (right - 1 >= 0) and (nums[right - 1] >= 0):
        right -= 1

    res = []
    while left >= 0 or right < len(nums):
        if left >= 0 and right < len(nums):
            if abs(nums[left]) > abs(nums[right]):
                res.append(pow(nums[right], 2))
                right += 1
            else:
                res.append(pow(nums[left], 2))
                left -= 1
        elif left >= 0:
            res.append(pow(nums[left], 2))
            left -= 1
        else:
            res.append(pow(nums[right], 2))
            right += 1

    return res

def solution2(nums):
    nums = [i**2 for i in nums]
    res = []


    return res

if __name__ == '__main__':
    nums = [-7, -3, 2, 3, 11]
