"""
파이썬의 장점을 살린 퀵 정렬 알고리즘
- 시간 복잡도 측면에서는 매번 pivot과 비교하여 비효율적이지만 직관적이고 기억하기 쉽다.
"""

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot] # 왼쪽 분할 부분
    right_side = [x for x in tail if x >= pivot] # 오른쪽 분할 부분

    # 분할 후 왼쪽과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))