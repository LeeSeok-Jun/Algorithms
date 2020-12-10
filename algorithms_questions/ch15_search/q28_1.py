"""
고정점 찾기 - 2회차
"""

# 풀이 제한 시간 : 20분
# 2020/12/10 10:43 ~ 11:01
# return을 빼먹음

n = int(input())
array = list(map(int, input().split()))

def binarySearch(array, start, end):
    if start >= end:
        return None

    mid = (start + end) // 2

    if mid == array[mid]:
        return mid

    elif mid < array[mid]:
        # 여기서 반드시 return을 넣어야 한다.
        return binarySearch(array, start, mid-1)
    else:
        # 여기서 반드시 return을 넣어야 한다.
        return binarySearch(array, mid+1, end)

answer = binarySearch(array, 0, n-1)

if answer == None:
    print(-1)
else:
    print(answer)