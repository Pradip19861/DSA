def count_frequency(a):
    freq = {}
    for i in a:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(count_frequency([1, 2, 3, 4, 2, 3, 3]))
