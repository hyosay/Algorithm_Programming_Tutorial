array = [1, 3, 2, 4, 3, 2, 5 ,3, 1, 2,
         3, 4, 4, 3, 5, 1, 2, 3, 5, 2,
         3, 1, 4, 3, 5, 1, 2, 1, 1, 1]
'''
count = [0] * max(array)

for i in range(0, len(array)):
    count[array[i] - 1] += 1

for i in range(0, len(count)):
    if count[i] != 0:
        for j in range(0, count[i]):
            print(i + 1, end= '')'''












count = [0] * max(array)
print(count)

for i in range(0, len(array)):
    count[array[i] - 1] += 1
print(count)

for i in range(0, len(count)):
    if count[i] != 0:
        for j in range(0, count[i]):
            print(i + 1, end= ' ')
