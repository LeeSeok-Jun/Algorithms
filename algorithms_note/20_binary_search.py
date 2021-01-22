"""
이진 탐색
- 시간 복잡도 O(logN)
- 사전에 배열이 정렬되어 있어야 한다.
"""

# 1. 재귀적 방법
def recursive_binary_search(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    if array[mid] == target:
        return mid

    elif array[mid] < target:
        return recursive_binary_search(array, target, mid+1, end)

    else:
        return recursive_binary_search(array, target, start, mid-1)


# 2. 반복문을 이용한 방법
def iterative_binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        
        elif array[mid] < target:
            start = mid + 1

        else:
            end = mid - 1

    return None


# 파이썬 라이브러리 함수 bisect
# 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적
# 시간 복잡도 O(logN)에 동작

from bisect import bisect_left, bisect_right

a = [1, 2, 3, 4, 5]
x = 4

print(bisect_left(a, x))
# 2

print(bisect_right(a, x))
# 4

# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    return right_index - left_index

array = [1, 2, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(array, 4, 4))
# 2

print(count_by_range(array, -1, 3))
# 6