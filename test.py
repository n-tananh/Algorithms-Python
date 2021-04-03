# nums = [-4, -1, 0, 3, 10]
nums = [-1]

left = -1
for i in range(0, len(nums)):
    if nums[i] < 0:
        left += 1
    else:
        break

print(left)