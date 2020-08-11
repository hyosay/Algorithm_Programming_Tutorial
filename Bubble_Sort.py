#시간 복잡도는 떨어진다.
#버블 정렬
# N * (N + 1) / 2

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

for i in range(0, len(array)):
    for j in range(0, len(array) - i - 1):
        if array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
    print(array)