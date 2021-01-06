"""
선택 정렬
- 시간 복잡도 O(N^2) : 2중 반복문으로 구현
"""

array = [3, 5, 8, 0, 1, 4, 2, 7, 6]
n = len(array)

for i in range(n):
    min_index = i
    for j in range(i+1, n):
        # i 이후 배열의 값 중 제일 작은 값을 찾음
        if array[j] < array[min_index]:
            min_index = j

    # 이 과정에서 오름차순으로 정렬된다.
    array[i], array[min_index] = array[min_index], array[i]

print(array)