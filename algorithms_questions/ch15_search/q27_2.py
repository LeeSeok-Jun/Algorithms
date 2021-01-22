"""
정렬된 배열에서 특정 수의 개수 구하기 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/22 13:19 ~ 13:22
# 정답

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())

data = list(map(int, input().split()))

answer = count_by_range(data, x, x)

if answer == 0:
    print(-1)
else:
    print(answer)
