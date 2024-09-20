def oddevensum(n):
    even = 0
    odd = 0
    for i in range(len(n)):
        if n[i] % 2 == 0:
            even += n[i]
        else:
            odd += n[i]
    print(even)
    print(odd)

n = [1, 2, 3, 4, 5, 6]
print(oddevensum(n))