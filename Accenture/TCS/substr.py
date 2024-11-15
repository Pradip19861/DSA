s = input()
j = 1
c = 0
while j < len(s):
    if ord(s[c]) < ord(s[j]):
        c = j
    j += 1

print(s[c:])