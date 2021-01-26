"""
숨바꼭질 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/26 16:18 ~ 16:33
# 알고리즘은 맞았는데 거리 정보 증가하는 단계에서 해설 코드와 다름(주석 처리)

import heapq
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # graph[a].append(b)
    # graph[b].append(a)
    graph[a].append((b, 1))
    graph[b].append((a, 1))

INF = int(1e9)
distance = [INF] * (n + 1)
distance[1] = 0

q = []
heapq.heappush(q, (0, 1))

while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
        continue

    for i in graph[now]:
        # cost = dist + 1
        cost = dist + i[1]

        # if cost < distance[i]:
        if cost < distance[i[0]]:
            # distance[i] = cost
            distance[i[0]] = cost
            # heapq.heappush(q, (cost, i))
            heapq.heappush(q, (cost, i[0]))

"""
# 내가 생각한 방법
hiding = INF
hiding_distance = max(distance[1:])
same_distance = 0

for i in range(1, n+1):
    if distance[i] == hiding_distance:
        hiding = min(hiding, i)
        same_distance += 1

print(hiding, hiding_distance, same_distance)
"""

hiding = 0
hiding_distance = 0
same_distance = []

for i in range(1, n+1):
    if hiding_distance < distance[i]:
        hiding = i
        hiding_distance = distance[i]
        same_distance = [hiding]
    elif hiding_distance == distance[i]:
        same_distance.append(i)

print(hiding, hiding_distance, len(same_distance))