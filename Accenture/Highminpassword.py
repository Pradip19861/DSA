def highminpassword(arr: list) -> tuple:
    arr.sort()
    res = []
    count = 1

    for i in range(len(arr) - 1):
        if arr[i] == arr[i + 1]:
            count += 1
        else:
            if count > 1:
                res.append(count)
            count = 1
    if count > 1:
        res.append(count)

    res.sort()

    if len(res) < 2:
        return (0, 0)
    else:
        return (res[-2], res[-1])

print(highminpassword([12, 13, 14, 15, 16, 17, 18, 19]))
print(highminpassword([12, 13, 13, 14, 14, 14, 15, 16, 17, 18, 19]))
