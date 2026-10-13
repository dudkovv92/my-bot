def bubble(nums):
    n = len(nums)
    for i in range(n):
        for j in range(n - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums

print(bubble([3, 1, 4, 1, 5, 9, 2, 6]))