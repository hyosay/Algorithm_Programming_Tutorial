number = 10
data = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
def quickSort(a, start, end):
    if start >= end:
        return

    pivot = start
    L = start
    R = end

    while L < R:
        while a[L] > a[pivot]:
            L = L + 1
        while a[R] < a[pivot] and R > start:
            R = R - 1

        if L > R:
            a[L], a[R] = a[R], a[L]
        else:
            a[pivot], a[R] = a[R], a[pivot]

    quickSort(a, start, R - 1)
    quickSort(a,L + 1, end)


quickSort(data, 0, 9)
print(data)









