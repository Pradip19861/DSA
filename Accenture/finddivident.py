def divideent(A, D, Q, R):
    divident = D * Q + R
    for i in range(len(A)):
        if A[i] == divident:
            return i
    return -1 

A = list(map(int, input("Enter the array elements separated by space: ").split()))

D = int(input("Enter D: "))
Q = int(input("Enter Q: "))
R = int(input("Enter R: "))

print(divideent(A, D, Q, R))