def findNumbers(nums) -> int:
    count = 0
    for num in range(len(nums)):
        if len(str(nums[num])) % 2 == 0:
            count += 1
    return count

if __name__ == '__main__':
    nums = [555, 901, 482, 1771]
    res = findNumbers(nums)
    print(res)