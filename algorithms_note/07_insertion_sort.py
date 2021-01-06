"""
삽입 정렬
- 일반적인 경우 시간 복잡도 O(N^2)
- 최선의 경우 O(N) : 대부분 정렬되어 있는 경우 해당
"""

array = [3, 5, 8, 0, 1, 4, 2, 7, 6]
n = len(array)

for i in range(1, n):
    # 선택 정렬과 다르게 뒤에서 앞으로 이동하면서 비교
    for j in range(i, 0, -1):
        # 현재 원소와 그 앞 원소를 비교하여 앞의 원소가 더 큰 경우 교체
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]

        # 현재 원소가 앞의 원소보다 큰 경우 더 이상 검사할 필요 없음
        else:
            break

print(array)