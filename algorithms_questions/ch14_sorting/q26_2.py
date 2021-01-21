"""
카드 정렬하기 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/21 14:57 ~ 15:15
# 실패 - 틀린 부분 주석 처리

import heapq

n = int(input())

data = []
for _ in range(n):
    heapq.heappush(data, int(input()))

"""
sum_value = heapq.heappop(data)

while data:
    now = heapq.heappop(data)

    sum_value += now
    heapq.heappush(data, sum_value)

print(sum_value)
"""

result = 0

while len(data) != 1:
    one = heapq.heappop(data)
    two = heapq.heappop(data)

    sum_value = one + two
    result += sum_value

    heapq.heappush(data, result)

print(result)
