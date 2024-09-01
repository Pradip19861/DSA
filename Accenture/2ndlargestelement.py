def count_second_largest(a):
    a.sort(reverse=True)
    largest = a[0]
    second_largest = None

    for i in range(1, len(a)):
        if a[i] != largest:
            second_largest = a[i]
            break
    if second_largest is not None:
        return a.count(second_largest)
    else:
        return 0
print(count_second_largest([10, 20, 30, 40, 50]))  # Expected output: 1
print(count_second_largest([10, 20, 30, 40, 40, 50]))  # Expected output: 2
