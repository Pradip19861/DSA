def timeinterval(l1, l2, s):
    distence = l1+l2
    speed = s*(5/18)
    time = distence / speed
    return round(time)

print(timeinterval(400, 400, 18))