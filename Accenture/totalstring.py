def totalstring(s):
    res = 0
    for i in range(len(s)):
        if s[i] != " ":
            res += 1
    return res

print(totalstring("total land total"))  # Output will be 13
