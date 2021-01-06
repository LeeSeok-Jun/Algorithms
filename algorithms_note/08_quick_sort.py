"""
퀵 정렬
- 평균 시간 복잡도 O(NlogN)
- 최악의 경우 시간 복잡도 O(N^2)
    * 삽입 정렬과 반대로 데이터가 어느 정도 정렬 되어있는 경우 느리게 동작

알고리즘 진행 과정
    1. 리스트 안의 한 원소를 선택한다. 이 원소를 피벗(pivot)이라고 한다.
    2. 피벗을 기준으로 작은 원소는 모두 피벗의 좌측으로, 큰 원소는 피벗의 우측으로 옮긴다.
    3. 피벗을 제외한 분할된 좌우측의 원소들을 정렬한다.
        * 분할된 원소들을 정렬할 때, 재귀 호출을 이용하여 1~3 과정을 통해 정렬한다.
    4. 분할된 리스트들이 더 이상 분할이 불가능할 때 까지 위 과정을 반복한다.
        * 분할된 리스트의 크기가 0이나 1이 될 때 까지 반복
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
n = len(array)

# 1. 일반적으로 구현한 퀵 정렬 알고리즘

def quick_sort(array, start, end):
    # 원소가 1개 이하인 경우 종료
    if start >= end:
        return

    # 피벗 원소를 첫 번째 원소로 지정
    pivot = start

    left = start + 1
    right = end

    while left < right:
        # 피벗 원소보다 큰 원소 찾기
        while left <= end and array[left] <= array[pivot]:
            left += 1

        # 피벗 원소보다 작은 원소 찾기
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # left는 피벗 원소보다 큰 원소를 가리키고
        # right는 피벗 원소보다 작은 원소를 가리키는 중

        # 두 탐색 인덱스가 엇갈린다면 피벗을 작은 원소와 교체 후 반복이 종료됨
        # 이 경우 right 인덱스가 원소가 리스트를 분할하는 기준이 된다.
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]

        # 엇갈리지 않은 경우 피벗 보다 큰 원소와 작은 원소의 위치 교체
        # 일반적인 경우에 해당
        else:
            array[left], array[right] = array[right], array[left]

    # 리스트를 기준의 좌, 우로 분할하여 재귀 호출로 각각 정렬 수행
    quick_sort(array, start, right-1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, n-1)
print(array)


# 2. 파이썬의 장점을 살린 퀵 정렬 알고리즘
# 시간 복잡도 측면에서는 위 방법보다 비효율적

def quick_sort_python(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [ x for x in tail if x <= pivot]
    right_side = [ x for x in tail if x >= pivot]

    return quick_sort_python(left_side) + [pivot] + quick_sort_python(right_side)

print(quick_sort_python(array))