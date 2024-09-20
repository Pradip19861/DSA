def lenoflast(s):
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
            count = 0
        else:
            count += 1
    return count

print(lenoflast("Hello World"))  # Output: 5