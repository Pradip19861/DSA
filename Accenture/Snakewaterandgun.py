try:
    n = int(input("Enter the number: "))
except ValueError:
    print("Please enter a valid integer.")
    exit()

s = input("Enter the string: ")

def solve(n, s):
    A = ""
    B = ""
    word = ""
    flag = False
    
    for i in range(len(s)):
        word += s[i]
        
        if word == "snake":
            if flag:
                B += "s"
            else:
                A += "s"
            flag = not flag
            word = ""
        elif word == "water":
            if flag:
                B += "w"
            else:
                A += "w"
            flag = not flag
            word = ""
        elif word == "gun":
            if flag:
                B += "g"
            else:
                A += "g"
            flag = not flag
            word = ""
    
    print(A)
    print(B)
    
    c = 0
    for i in range(n):
        if (B[i] == 's' and A[i] == 'g') or (B[i] == 'w' and A[i] == 's') or (B[i] == 'g' and A[i] == 'w'):
            c += 1
            
    return c

print(solve(n, s))
