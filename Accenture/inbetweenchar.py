def inbetween(s):
    if len(s) >= 10:
        count = len(s) - 2
        res = s[0] + str(count) + s[-1]
    else:
        res = s
    return res

print(inbetween("understandable"))