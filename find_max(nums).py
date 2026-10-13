def find_min(nums):
    min_num = nums[0]
    for n in nums:
        if n < min_num:
             min_num = n
    return min_num

print(find_min([-5, -1, -10]))