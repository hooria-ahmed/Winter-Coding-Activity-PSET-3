def repeated_n_times_basic(nums):
    freq = {}
    n = len(nums) // 2

    for x in nums:
        freq[x] = freq.get(x, 0) + 1
        if freq[x] == n:
            return x


nums = [2, 1, 2, 5, 3, 2]
print(repeated_n_times_basic(nums))
# Expected: 2

nums = [5, 1, 5, 2, 5, 3]
print(repeated_n_times_basic(nums))
# Expected: 5

nums = [7, 7, 7, 4, 1, 2]
print(repeated_n_times_basic(nums))
# Expected: 7
