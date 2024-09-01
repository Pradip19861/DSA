def stringreplace(s, ch1, ch2):
    s = list(s)
    for i in range(len(s)):
        if s[i] == ch1:
            s[i] = ch2
        elif s[i] == ch2:
            s[i] = ch1
    return ''.join(s)
s = input("")
ch1 = input("")
ch2 = input("")
result = stringreplace(s, ch1, ch2)
print("",result)