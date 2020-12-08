"""
정렬된 배열에서 특정 수의 개수 구하기 - 문제 해설
- bisect 외장 라이브러리 없이 해결하는 방법
"""

# 특정 수의 처음 위치를 탐색
def first(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    # 여러개의 특정 수 중 가장 왼쪽에 있는 수의 인덱스만 반환
    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid

    elif target < array[mid]:
        return first(array, target, start, mid-1)

    else:
        return first(array, target, mid+1, end)

# 특정 수의 마지막 위치 탐색
def last(array, target, start, end):
    if start > end:
        return None

    mid = (start + end) // 2

    # 여러개의 특정 수 중 가장 오른쪽에 있는 수의 인덱스만 반환
    if (mid == n - 1 or target < array[mid + 1]) and array[mid] == target:
        return mid
    
    elif target < array[mid]:
        return last(array, target, start, mid-1)

    else:
        return last(array, target, mid+1, end)

# 특정 수의 출현 횟수를 구함
def count_by_value(array, x):
    n = len(array)

    # 특정 수가 처음 등장하는 인덱스
    a = first(array, x, 0, n-1)

    # 특정 수가 없다면
    if a == None:
        return 0

    # 특정 수가 마지막으로 등장하는 인덱스
    b = last(array, x, 0, n-1)

    return b - a + 1


n, x = map(int, input().split())
array = list(map(int, input().split()))

count = count_by_value(array, x)

if count == 0:
    print(-1)
else:
    print(count)

