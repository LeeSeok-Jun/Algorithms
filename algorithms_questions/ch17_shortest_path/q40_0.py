"""
숨바꼭질
- 동빈이는 술래로 부터 도망치기 위해 1~N번 까지의 헛간 중 하나에 숨을 수 있다.
- 술래는 항상 1번 헛간에서 출발하여 동빈이를 찾는다.
- 전체 맵에는 총 M개의 양방향 통로가 존재하며 하나의 통로는 다른 두 헛간을 연결한다.
- 전체 맵은 항상 어떤 헛간에서 다른 어떤 헛간으로 도달이 가능한 형태로 주어진다.
- 동빈이가 1번 헛간으로 부터 최단 거리가 가장 먼 헛간이 가장 안전하다고 판단한다.
    * 최단 거리는 지나야 하는 길의 최소 개수를 의미한다.
- 동빈이가 숨을 헛간의 번호를 출력하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에는 N과 M이 주어지며, 공백으로 구분한다.
- 이후 M개의 줄에 걸쳐 서로 연결된 두 헛간 A와 B의 번호가 공백으로 구분되어 주어진다.

출력 조건
- 첫 번째는 숨어야 하는 헛간 번호를 출력한다.
- 두 번째는 그 헛간까지의 거리를 출력한다.
- 세 번째는 그 헛간과 같은 거리를 갖는 헌산의 개수를 출력한다.
"""

# 풀이 제한 시간 : 40분
# 20202/12/23 10:34 ~ 10:48
# 출력 조건을 찾는 방법 실패

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

distance = [INF] * (n+1)

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


dijkstra(1)

max_node = 0
max_distance = 0
result = []

for i in range(1, n+1):
    if max_distance < distance[i]:
        max_node = i
        max_distance = distance[i]
        result = [max_node] # 새로운 최대값 노드가 발견되면 기존 리스트는 삭제되고 새롭게 작성됨
    elif max_distance == distance[i]:
        result.append(i)

print(max_node, max_distance, len(result))