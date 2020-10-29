"""
퀵 정렬 알고리즘(일반적인 형태)
- 평균 시간 복잡도 O(NlogN)
- 최악의 경우 시간 복잡도 O(N^2)
- 삽입 정렬과 다르게 데이터가 어느정도 정렬 되어있는 경우 느리게 동작
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    pivot = start # 첫 번째 원소를 피벗(pivot, 기준)으로 지정
    left = start + 1
    right = end
    while left < right:
        # 피벗보다 큰 데이터를 찾을때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 두 인덱스가 엇갈린다면 피벗을 작은 데이터와 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않은 경우 작은 데이터와 큰 데이터의 위치 교체
            array[left], array[right] = array[right], array[left]
    # 리스트를 기준의 좌 우로 분할하여 각각 정렬 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)