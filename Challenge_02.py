def min_boats_basic(weights, priority, limit):
    n = len(weights)
    used = [False] * n
    boats = 0

    for i in range(n):
        if used[i]:
            continue

        used[i] = True
        paired = False

        for j in range(i + 1, n):
            if not used[j]:
                if weights[i] + weights[j] <= limit:
                    if not (priority[i] == 1 and priority[j] == 1):
                        used[j] = True
                        paired = True
                        break

        boats += 1

    return boats



weights  = [30, 50, 60, 40, 70, 80]
priority = [1, 0, 1, 0, 0, 1]
limit = 100

# Expected: 4
print(min_boats_basic(weights, priority, limit))
