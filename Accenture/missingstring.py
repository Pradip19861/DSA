def find_misplaced_character(s):
    for i in range(len(s) - 1):
        if ord(s[i]) > ord(s[i + 1]):
            return s[i]
        elif ord(s[i]) > ord(s[i + 1]):
            return s[i+1]
    return None
print(find_misplaced_character("efgah"))