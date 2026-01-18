def evacuation_system(weights, priority, limit, queries):
    n = len(weights)

    # Separate people
    priority_people = []
    normal_people = []

    for i in range(n):
        if priority[i] == 1:
            priority_people.append(weights[i])
        else:
            normal_people.append(weights[i])

    priority_people.sort()
    normal_people.sort()

    boats = 0
    i = 0
    j = len(normal_people) - 1

    # Pair priority with normal if possible
    for w in priority_people:
        while j >= i and normal_people[j] + w > limit:
            j -= 1

        if j >= i:
            j -= 1  # paired
        boats += 1  # priority always uses a boat

    # Remaining normal people
    remaining = j - i + 1
    boats += (remaining + 1) // 2

    # --- Queries ---
    results = []
    total_people = n

    for q in queries:
        parts = q.split()

        if parts[0] == "CANPAIR":
            x, y = int(parts[1]), int(parts[2])
            if weights[x] + weights[y] <= limit and not (priority[x] == 1 and priority[y] == 1):
                results.append("Yes")
            else:
                results.append("No")

        elif parts[0] == "REMAINING":
            B = int(parts[1])
            evacuated = min(total_people, 2 * B)
            results.append(str(total_people - evacuated))

    return boats, results




weights  = [30, 50, 60, 40, 70, 80]
priority = [1, 0, 1, 0, 0, 1]
limit = 100

queries = [
    "CANPAIR 0 1",
    "CANPAIR 0 2",
    "REMAINING 2"
]
boats, answers = evacuation_system(weights, priority, limit, queries)

print("Minimum boats =", boats)
for ans in answers:
    print(ans)

