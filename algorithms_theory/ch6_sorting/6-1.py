"""
선택 정렬
- 시간 복잡도 O(N^2) : 직관적으로 2중 반복문 사용으로 이해 가능하다.
- 비효율적이지만 가장 작은 데이터를 찾을 때 이 형태에 익숙해질 필요가 있다.
"""
# 2020/10/10

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i # 가장 작은 원소의 인덱스
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j # 실제 가장 작은 원소의 인덱스
    array[i], array[min_index] = array[min_index], array[i] # 현재 탐색 중인 자료와 위치 교환(스와프)


print(array)