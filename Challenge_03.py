def broadcast_simple(N, K, operations):
    subs = [set() for _ in range(N + 1)]
    messages = []  # (id, sender, critical)
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
            messages.append((msg_id, u, critical))

        elif parts[0] == 'F':
            u = int(parts[1])
            feed = []

            for mid, sender, critical in reversed(messages):
                if sender == u or sender in subs[u]:
                    feed.append(mid)
                if len(feed) == 10:
                    break

            if feed:
                print(*feed)
            else:
                print("EMPTY")


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

broadcast_simple(N, K, ops)
