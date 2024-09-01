s = "101"  # This should be a string input, not using input(101)
res = ""
count = 0 

for c in s:
    if c == '0' and count == 0:
        count = 0
    elif c == '0' and count > 0:
        res += chr(ord('A') + count - 1)
        count = 0
    else:
        count += 1

if s[-1] == '1':  # Check the last character
    res += chr(ord('A') + count - 1)

print(res)
