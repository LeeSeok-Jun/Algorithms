"""
가사 검색
- https://programmers.co.kr/learn/courses/30/lessons/60060
"""

# 풀이 제한 시간 : 1시간 30분
# 2020/12/09 11:22 ~
# 실패 - 문제 접근 방법을 생각하지 못했음

from bisect import bisect_left, bisect_right

def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)

    return right_index - left_index

# 모든 단어를 길이마다 나누어 저장
array = [[] for _ in range(10001)] # 단어의 최대 길이는 10000
# 모든 단어를 뒤집어서 저장
reversed_array = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words:
        array[len(word)].append(word) # 길이가 n인 단어는 array[n]에 저장
        reversed_array[len(word)].append(word[::-1]) # 길이가 n인 단어를 뒤집어서 reversed_array[n]에 저장

    # 각 배열을 정렬 수행
    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    # 각각의 쿼리에 대해서 처리
    for q in queries:
        # 접두사 검색 (접미사에 ?가 붙은 경우)
        if q[0] != '?':
            # ?를 a와 z로 치환하여 queyr길이와 같은 단어 장에서 이진 탐색을 통해 접두사가 포함된 단어의 개수 확인 
            result = count_by_range(array[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        # 접미사 검색 (접두사에 ?가 붙은 경우)
        else:
            # 쿼리를 뒤집고 똑같이 ?를 a와 z로 치환하여 같은 길이를 같는 뒤집힌 단어장에서 단어의 개수 확인
            result = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))

        answer.append(result)

    return answer