# Kadane's Algorithm

def maxSub(nums):
    max_sum = nums[0]
    current_sum = max_sum
    for i in range(1, len(nums)):
        current_sum = max(nums[i], nums[i] + current_sum)
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


if __name__ == '__main__':
    nums = [5,4,-1,7,8]
    print(maxSub(nums))