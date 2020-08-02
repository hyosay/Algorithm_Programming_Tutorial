number = 10
data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
def quickSort(*data, start, end): #0, 9
    if start >= end:
        return;
    key = start
    i = start + 1
    j = end
    temp = 0

    while i <= j:
        while data[i] <= data[key]:
            i = i + 1
        while data[j] >= data[key] and j > start:
            j = j - 1
        if i > j:
            data[j], data[key] = data[key], data[j]
        else:
            data[j], data[i] = data[i], data[j]

    quickSort(data, start, j - 1)
    quickSort(data, j + 1, end)


quickSort(data, 0, number - 1)


