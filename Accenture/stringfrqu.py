def stringfreq():
    n = int(input())
    arr =input().split()
    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    max_freq = 0
    result = ""
    for i in freq:
        if freq[i] > max_freq:
            max_freq = freq[i]
            result = i
    return result