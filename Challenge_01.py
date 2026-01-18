def alert_basic(temp, K):
    n = len(temp)
    res = [0] * n
    for i in range(n):
        for j in range(i+1, n):
            if temp[j] >= temp[i] + K or temp[j] <= temp[i] - K:
                res[i] = j
                break
    return res


# Test Case 1
temp = [30, 31, 29, 35]
K = 3
print(alert_basic(temp, K))
# Expected: [3, 3, 3, 0]

# Test Case 2
temp = [20, 21, 22, 23]
K = 5
print(alert_basic(temp, K))
# Expected: [0, 0, 0, 0]

# Test Case 3
temp = [10, 20, 15]
K = 5
print(alert_basic(temp, K))
# Expected: [1, 2, 0]

# Test Case 4
temp = [25]
K = 3
print(alert_basic(temp, K))
# Expected: [0]

# Test Case 5
temp = [40, 35, 45]
K = 5
print(alert_basic(temp, K))
# Expected: [1, 2, 0]

# Test Case 6
temp = [50, 45, 40, 35]
K = 4
print(alert_basic(temp, K))
# Expected: [1, 2, 3, 0]

# Test Case 7
temp = [10, 10, 10, 10]
K = 0
print(alert_basic(temp, K))
# Expected: [1, 1, 1, 0]


