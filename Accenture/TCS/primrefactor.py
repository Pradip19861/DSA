def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def primefactors(n):
    sumfactors = 0
    for i in range(2, n+1):
        if n % i == 0 and isprime(i):
            sumfactors += i
    return sumfactors

print(primefactors(20))