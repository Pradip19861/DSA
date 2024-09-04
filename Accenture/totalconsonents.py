def permutationcom(s):
    l = ["a",
         "e",
         "i",
         "o",
         "u"]
    count = 0
    count1 = 0
    x = len(s)
    b = sorted(s)
    for i in range(len(b)-1):
        if b[i] == b[i + 1]:
            count1 += 1
            fact1 = 1
            for i in range(1, count1 + 1):
                fact1 *= i
        if b[i] in l:
            count += 1
        y = x - count
    fact = 1
    for i in range(1, y + 1):
        fact*= i
    
    return fact /fact1
s = input()
print(permutationcom(s))