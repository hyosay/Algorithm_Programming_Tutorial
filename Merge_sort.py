def mergeSort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left_arr = mergeSort(a[:mid])
    right_arr = mergeSort(a[mid:])

    merged_arr = []
    i = j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            merged_arr.append(left_arr[i])
            i += 1
        else:
            merged_arr.append(right_arr[j])
            j += 1


    #1. merged_arr += left_arr[i:]
    while i < len(left_arr):
        merged_arr.append(left_arr[i])
        i += 1
    while j < len(right_arr):
        merged_arr.append(right_arr[j])
        j += 1
    #2.merged_arr += right_arr[j:]
    print(merged_arr)
    return merged_arr

array = [6, 8, 3, 9, 10, 1, 2, 4]
print(mergeSort(array))


