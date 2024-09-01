def divquesremai(arr, div, ques, rem):
    divitent = div*ques+rem
    for i in range(len(arr)):
        if arr[i] == divitent:
            return i
    return -1
print(divquesremai([1,2,3,4], 1, 1, 1))