def findBestRhyme(S, D, length):
    best_word = "No Word"
    max_match_length = 0
    
    for word in D:
        if word == S:
            continue
        match_length = 0
        min_len = min(len(S), len(word))
        for i in range(1, min_len + 1):
            if S[-i] == word[-i]:
                match_length += 1
            else:
                break
        if match_length > max_match_length:
            max_match_length = match_length
            best_word = word
    
    return best_word
S = "typical"
D = ["critical", "radical", "logical", "typical"]
length = len(D)
print(findBestRhyme(S, D, length))
