def checkprime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

num = int(input("Enter a number: "))
s = 0
while num > 0:
    digit = num % 10
    s += digit
    num= num // 10  # Corrected this line to use integer division by 10

ans = checkprime(s)
print(ans)
