def find_anagrams_basic(s, p):
    res = []
    p_count = {}

    for ch in p:
        p_count[ch] = p_count.get(ch, 0) + 1

    m = len(p)

    for i in range(len(s) - m + 1):
        window = s[i:i+m]
        w_count = {}

        for ch in window:
            w_count[ch] = w_count.get(ch, 0) + 1

        if w_count == p_count:
            res.append(i)

    return res


s = "cbaebabacd"
p = "abc"
find_anagrams_basic(s, p)
# Expected: [0, 6]

s = "abab"
p = "ab"
find_anagrams_basic(s, p)
# Expected: [0, 1, 2]

s = "aaaaa"
p = "aa"
find_anagrams_basic(s, p)
# Expected
# : [0, 1, 2, 3]
