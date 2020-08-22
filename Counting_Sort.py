'''
count = [0] * max(array)

for i in range(0, len(array)):
    count[array[i] - 1] += 1

for i in range(0, len(count)):
    if count[i] != 0:
        for j in range(0, count[i]):
            print(i + 1, end= '')'''




'''count = [0] * (max(array) + 1)
print(count)

for i in range(0, len(array)):
    count[array[i]] += 1


for i in range(0, len(count)):
    for j in range(0, count[i]):
        print(i + 1, end= ' ')'''
# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 3, 1, 6, 2, 9, 1, 4, 8, 5, 2]
# 모든 범위를 포함하는 리스트 선언 (모든 값은 0으로 초기화)
count = [0] * (max(array) + 1)

for i in range(len(array)):
    count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가
print(count)
for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
        print(i, end= ' ')