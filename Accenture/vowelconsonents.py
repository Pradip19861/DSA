def value(s):
    vowels = ["a", "e", "i", "o", "u"]
    res = ""
    
    for i in range(len(s)):
        if s[i] in vowels:
            # Check boundaries and ensure the next and previous characters are not vowels
            if (i == 0 or s[i - 1] not in vowels) and (i == len(s) - 1 or s[i + 1] not in vowels):
                res += s[i]
    return res

print(value("abec"))  # Output: "ae"