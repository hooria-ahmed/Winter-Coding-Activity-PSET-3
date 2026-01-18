def longest_palindrome_optimized(s):
    if not s:
        return ""

    start = 0
    max_len = 1
    n = len(s)

    def expand(l, r):
        nonlocal start, max_len
        while l >= 0 and r < n and s[l] == s[r]:
            if r - l + 1 > max_len:
                start = l
                max_len = r - l + 1
            l -= 1
            r += 1

    for i in range(n):
        expand(i, i)       # odd length
        expand(i, i + 1)   # even length

    return s[start:start + max_len]


s = "babad"
print(longest_palindrome_optimized(s))
# Expected: "bab" or "aba"

s = "cbbd"
print(longest_palindrome_optimized(s))
# Expected: "bb"

s = "a"
print(longest_palindrome_optimized(s))
# Expected: "a"
