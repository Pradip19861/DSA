def reboundedhight(H,V1,V2):
    e = V1/V2
    Rebound = H * pow(e,2)
    return round(Rebound)
H = int(input())

V1 = int(input())

V2 = int(input())
print(reboundedhight(H,V1,V2))