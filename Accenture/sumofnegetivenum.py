def sum_of_negative_nums(a, b, c, d):
    sum = 0
    if a <= 0:
        sum += a
    if b <= 0:
        sum += b
    if c <= 0:
        sum += c
    if d <= 0:
        sum += d
    return sum
print(sum_of_negative_nums(-5, -5, -5, -5))
