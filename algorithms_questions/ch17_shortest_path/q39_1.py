"""
화성 탐사 - 2회차
"""

# 풀이 제한 시간 : 40분
# 2020/12/24 10:25 ~ 10:40
# 실패 - 다익스트라 알고리즘 구현 미숙

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(int(input())):

    n = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    distance = [[INF] * n for _ in range(n)]

    q = [(graph[0][0], 0, 0)]
    # 빠진 부분
    distance[0][0] = graph[0][0]

    while q:

        # dist, r, c = q.heappop()
        dist, r, c = heapq.heappop(q)

        # 부등호 반대
        # if dist < distance[r][c]:
        #     continue

        if distance[r][c] < dist:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= n:
                continue

            cost = dist + graph[nr][nc]

            if cost < distance[nr][nc]:
                distance[nr][nc] = cost
                # q.heappush((graph[nr][nc], nr, nc))
                heapq.heappush(q, (cost, nr, nc))

    print(distance[n-1][n-1])

