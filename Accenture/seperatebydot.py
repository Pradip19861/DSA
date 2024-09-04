def separatebydot(s):
    a = s.split('.')
    largest = max(a, key=len)
    return largest.strip()
s = input()
print(separatebydot(s))  # Expected output: 789
