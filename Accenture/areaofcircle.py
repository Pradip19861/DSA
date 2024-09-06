def area_of_circle(r):
    area = 3.14 * r * r
    return round(area)  # Rounding to 2 decimal places
n = int(input().strip())
print(area_of_circle(n))
