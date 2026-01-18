def find_anagrams_optimized(s, p):
    res = []
    if len(p) > len(s):
        return res

    p_count = [0] * 26
    win_count = [0] * 26

    for ch in p:
        p_count[ord(ch) - ord('a')] += 1

    m = len(p)

    for i in range(len(s)):
        win_count[ord(s[i]) - ord('a')] += 1

        if i >= m:
            win_count[ord(s[i - m]) - ord('a')] -= 1

        if win_count == p_count:
            res.append(i - m + 1)

    return res


s = "cbaebabacd"
p = "abc"
print(find_anagrams_optimized(s, p))
# Expected: [0, 6]

s = "abab"
p = "ab"
print(find_anagrams_optimized(s, p))
# Expected: [0, 1, 2]

s = "aaaaa"
p = "aa"
print(find_anagrams_optimized(s, p))
# Expected
# : [0, 1, 2, 3]
