
def findMaxConsecutiveOnes(nums):
    max_count = 0
    count = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            max_count = [count, max_count][max_count > count]
        else:
            count = 0

    return max_count

if __name__ == '__main__':

    nums = [1, 1, 1, 1, 0]
    print(findMaxConsecutiveOnes(nums))