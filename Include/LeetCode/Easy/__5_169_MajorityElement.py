
def majorityElement1(nums):
    nums.sort()
    y = len(nums )//2
    n = nums[y]
    return n





# def majorityElement(self, nums):
#     candidate, count = nums[0], 0
#     for num in nums:
#         if num == candidate:
#             count += 1
#         elif count == 0:
#             candidate, count = num, 1
#         else:
#             count -= 1
#     return candidate
if __name__ == '__main__':

    nums = list(map(int, input().split()))
    print(majorityElement1(nums))
    # m = {}
# for n in nums:
#     m[n] = m.get(n, 0) + 1
#     if m[n] > len(nums) // 2:
#         print(n)

