"""
정렬된 배열에서 특정 수의 개수 구하기 - 2회차
"""

# 풀이 제한 시간 : 30분
# 2020/12/10 10:37 ~ 10:43
# 성공

from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
array = list(map(int, input().split()))

def countByArray(x):
    min_value = bisect_left(array, x)
    max_value = bisect_right(array, x)

    return max_value - min_value

answer = countByArray(x)

if answer == 0:
    print(-1)
else:
    print(answer)