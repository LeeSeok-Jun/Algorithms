"""
가사 검색 - 2회차
"""

# 풀이 제한 시간 : 1시간 30분
# 2020/12/10 11:16 ~ 11:26

from bisect import bisect_left, bisect_right

array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def countByRange(array, start, end):
    min_value = bisect_left(array, start)
    max_value = bisect_right(array, end)

    return max_value - min_value

def solution(words, queries):
    answer = []

    for word in words:
        array[len(word)].append(word)
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0] != '?':
            # array[len(q)] 빼먹음
            result = countByRange(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            answer.append(result)
        else:
            result = countByRange(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            answer.append(result)

    return answer