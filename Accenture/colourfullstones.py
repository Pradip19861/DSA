def colorfulstones(s, c):
    i = 0  # To track position in s
    j = 0  # To track position in c

    while j < len(c) and i < len(s):
        if s[i] == c[j]:
            i += 1
        j += 1

    return i + 1

# Test the function
print(colorfulstones("deeedbbcccbdaa", "abc"))  # Output will depend on the matching logic
