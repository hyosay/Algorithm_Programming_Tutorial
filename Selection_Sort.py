# selection sort는 N*2 시간복잡도 입니다.
# 효율성이 떨어진다.

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]
'''for i in range(0, 10):
    min = 9999
    for j in range(i, 10):
        if min > array[j]:
            min = array[j]
            index = j

    temp = array[i]
    array[i] = array[index]
    array[index] = temp

    array[i], array[index] = array[index], array[i]
    print(array)

'''




for i in range(0, len(array)):
    min = 9999
    for j in range(i, len(array)):
        if min > array[j]:
            min = array[j]
            index = j
    array[i], array[index] = array[index], array[i]
    print(array)