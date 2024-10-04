def strfreq(s):
    words = s.split()
    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    for word in freq:
        print(f"{word}: {freq[word]}")

strfreq("apple banana apple apple banana kela kela")