"""
숨바꼭질 - 2회차
"""

# 풀이 제한 시간 : 40분
# 20202/12/24 10:42 ~ 10:53
# 성공

import sys
import heapq

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

q = []
heapq.heappush(q, (0, 1))
distance[1] = 0

while q:
    dist , now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:

        cost = dist + i[1]

        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

max_index = 0
max_value = 0
same = []

for i in range(1, n+1):
    if distance[i] > max_value:
        max_index = i
        max_value = distance[i]
        same = [max_index]
    elif distance[i] == max_value:
        same.append(i)

print(max_index, max_value, len(same))