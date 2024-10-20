def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0: return 0
    last = {}
    for k in range(m):
        last[pattern[k]] = k
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i = i + m - min(k, j + 1)
            k = m - 1
    return -1
