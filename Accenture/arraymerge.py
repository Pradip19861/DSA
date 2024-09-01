def arraymerge(arr1, arr2):
    arr3 = arr1 + arr2  # Concatenate arr1 and arr2
    arr4 = []
    for i in range(len(arr3)):
        for j in range(i+1,len(arr3)):
            if arr3[i] > arr3[j]:
                arr4.append((arr3[j],arr3[i]))
            else:
                arr4.append((arr3[i],arr3[j]))
    return arr4 

print(arraymerge([1, 2, 3, 5], [4, 6, 7, 8]))