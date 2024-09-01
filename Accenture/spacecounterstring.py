def spacecounter(s1, s2):
    count1 = 0
    count2 = 0
    
    for i in range(len(s1)):
        if s1[i] == " ":
            count1 += 1
    
    for j in range(len(s2)):
        if s2[j] == " ":
            count2 += 1
    
    diff = count1 - count2
    return diff

print(spacecounter("abs ask same answer", "adw arg"))