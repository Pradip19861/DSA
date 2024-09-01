def reversechar(s):
    if len(s) < 2:
        return s 
    result = [] 
    i = 0
    while i < len(s) - 1:
        if s[i] != s[i + 1]:
            result.append(s[i])
        i += 1
    result.append(s[-1])
    return ''.join(result)
print(reversechar("aabbcc"))
print(reversechar("aabbcca"))
print(reversechar("aaaa"))
print(reversechar(""))    
print(reversechar("a"))