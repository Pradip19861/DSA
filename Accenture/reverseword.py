def reversewords(s):
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

print(reversewords("the sky is blue"))
print(reversewords("  hello world  "))
print(reversewords("a good   example"))