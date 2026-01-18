def alert_optimized(temp, K):
    n = len(temp)
    warm = [0] * n
    cold = [0] * n
    stack = []

    # Warmer alerts
    for i in range(n):
        while stack and temp[i] >= temp[stack[-1]] + K:
            warm[stack.pop()] = i
        stack.append(i)

    # Clear stack
    stack = []

    # Colder alerts
    for i in range(n):
        while stack and temp[i] <= temp[stack[-1]] - K:
            cold[stack.pop()] = i
        stack.append(i)

    # Final result
    res = [0] * n
    for i in range(n):
        candidates = []
        if warm[i] != 0:
            candidates.append(warm[i])
        if cold[i] != 0:
            candidates.append(cold[i])
        res[i] = min(candidates) if candidates else 0

    return res


# Test Case 1
temp = [30, 31, 29, 35]
K = 3
print(alert_optimized(temp, K))
# Expected: [3, 3, 3, 0]

# Test Case 2
temp = [20, 21, 22, 23]
K = 5
print(alert_optimized(temp, K))
# Expected: [0, 0, 0, 0]

# Test Case 3
temp = [10, 20, 15]
K = 5
print(alert_optimized(temp, K))
# Expected: [1, 2, 0]

# Test Case 4
temp = [25]
K = 3
print(alert_optimized(temp, K))
# Expected: [0]

# Test Case 5
temp = [40, 35, 45]
K = 5
print(alert_optimized(temp, K))
# Expected: [1, 2, 0]

# Test Case 6
temp = [50, 45, 40, 35]
K = 4
print(alert_optimized(temp, K))
# Expected: [1, 2, 3, 0]

# Test Case 7
temp = [10, 10, 10, 10]
K = 0
print(alert_optimized(temp, K))
# Expected: [1, 1, 1, 0]


