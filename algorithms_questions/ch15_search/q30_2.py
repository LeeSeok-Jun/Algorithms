"""
가사 검색 - 3회차
"""

# 풀이 제한 시간 : 1시간 30분
# 2021/01/22 14:29 ~ 15:11
# 실패

from bisect import bisect_left, bisect_right

# 내가 생각하지 못한 부분
array = [[] for _ in range(10001)]
reversed_array = [[] for _ in range(10001)]

def countByRange(array, start, end):
    left_value = bisect_left(array, start)
    right_value = bisect_right(array, end)

    return right_value - left_value

"""
def get_count(words, query):
    index = bisect_left(query, '?')
    count = 0

    for w in words:
        if len(query) == len(w) and query[:index+1] == w[:index+1]:
            count += 1

    return count
"""

def solution(words, queries):
    answer = []

    # reversed_words = []
    for w in words:
        array[len(w)].append(w)
        # reversed_words.append(w[::-1])
        reversed_array[len(w)].append(w[::-1])

    # 빼먹은 부분
    # 이진 탐색은 정렬된 배열에 대해서 작동한다 -> countByRange()에서 사용하기 위해 필요
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    # 필요 없는 코드
    # reversed_queries = []
    # for q in queries:
    #     reversed_queries.append(q[::-1])

    for q in queries:
        if q[0] != '?':
            # answer.append(get_count(words, q))
            result = countByRange(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
            answer.append(result)
        else:
            # reversed_query = q[::-1]
            # answer.append(get_count(reversed_words, reversed_query))
            result = countByRange(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
            answer.append(result)

    return answer