number = 10
a = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
def quickSort(a, start, end):
    if start >= end:
        return

    pivot = start
    L = start
    R = end

    while L <= R:
        while a[L] <= a[pivot]:
            L = L + 1
        while a[R] >= a[pivot] and R > start:
            R = R - 1
        if L > R:
            a[R], a[pivot] = a[pivot], a[R]
        else:
            a[R], a[L] = a[L], a[R]
    quickSort(a, start, R - 1)
    quickSort(a, L - 1, end)


quickSort(a, 0, number - 1)
print(a)







