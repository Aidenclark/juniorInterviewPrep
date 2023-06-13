def max_difference(nums):
    if len(nums) < 2:
        return 0
    min_num = nums[0]
    max_diff = 0
    for num in nums:
        if num < min_num:
            min_num = num
        elif num - min_num > max_diff:
            max_diff = num - min_num
    return max_diff
