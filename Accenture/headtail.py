def headtailgame(s):
    score = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "H":
            score += 2
            count += 1
        else:
            score -= 1
            count = 0
        
        if count == 3:
            return score

    return score

print(headtailgame("HTHTHHHHT"))  # Expected output: 5