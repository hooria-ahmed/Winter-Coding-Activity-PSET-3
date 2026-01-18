def broadcast_optimized(N, K, operations):
    subs = [set() for _ in range(N + 1)]
    user_msgs = [[] for _ in range(N + 1)]
    msg_id = 0

    for op in operations:
        parts = op.split()

        if parts[0] == 'S':
            u, v = int(parts[1]), int(parts[2])
            subs[u].add(v)

        elif parts[0] == 'U':
            u, v = int(parts[1]), int(parts[2])
            subs[u].discard(v)

        elif parts[0] == 'B':
            u, m = int(parts[1]), int(parts[2])
            msg_id += 1
            critical = (m % 3 == 0)

            user_msgs[u].append((msg_id, critical))
            if len(user_msgs[u]) > K:
                user_msgs[u].pop(0)

        elif parts[0] == 'F':
            u = int(parts[1])
            pool = []

            pool.extend(user_msgs[u])
            for v in subs[u]:
                pool.extend(user_msgs[v])

            if not pool:
                print("EMPTY")
                continue

            pool.sort(key=lambda x: (-x[0], -x[1]))
            result = [str(mid) for mid, _ in pool[:10]]
            print(" ".join(result))


N = 3
K = 2
ops = [
    "S 1 2",
    "S 1 3",
    "B 2 5",
    "B 3 9",
    "F 1",
    "U 1 2",
    "B 3 6",
    "F 1",
    "F 2"
]

broadcast_optimized(N, K, ops)

