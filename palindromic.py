def longestPalindromic(originStr):
    str = originStr.replace("", "#")
    center = 0
    right = 0
    p = dict()
    for i in range(1, len(str) - 1):
        i_mirror = center - (i - center)
        if right < i:
            p[i] = 0
        else:
            p[i] = p[i_mirror] if i_mirror > 0 else 0

        while i + 1 + p[i] < len(str) and str[i + 1 + p[i]] == str[i - 1 - p[i]]:
            p[i] = p[i] + 1

        if i + p[i] > right:
            center = i
            right = i + p[i]

    maxLen = 0
    for i in range(1, len(p)):
        if p[i] > maxLen:
            centerIndex = i
            maxLen = p[i]

    return originStr[(centerIndex - maxLen)/2:(centerIndex + maxLen)/2]

result = longestPalindromic("gabbcbbddbb")
print(result)
