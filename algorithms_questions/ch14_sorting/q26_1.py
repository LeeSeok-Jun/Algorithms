"""
카드 정렬하기 - 2회차
"""

# 풀이 제한 시간 : 30분
# 2020/12/04 11:20 ~ 11:25
# 우선순위 큐 사용법에 대해 숙지할 필요가 있다!

import heapq

n = int(input())

heap = []
for _ in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:

    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    summary = one + two
    result = result + summary

    heapq.heappush(heap, summary)

print(result)