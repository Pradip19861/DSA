def maxfrequency(s):
    count = 0
    max = 0
    char = ""
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        if count > max:
            max = count
            char = s[i]
    return char
print(maxfrequency("programming"))
