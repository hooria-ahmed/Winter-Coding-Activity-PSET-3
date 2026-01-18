def repeated_n_times_optimized(nums):
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    for i in range(len(nums) - 2):
        if nums[i] == nums[i + 2]:
            return nums[i]

    return nums[0]


nums = [2, 1, 2, 5, 3, 2]
print(repeated_n_times_optimized(nums))
# Expected: 2

nums = [5, 1, 5, 2, 5, 3]
print(repeated_n_times_optimized(nums))
# Expected: 5

nums = [7, 7, 7, 4, 1, 2]
print(repeated_n_times_optimized(nums))
# Expected: 7
