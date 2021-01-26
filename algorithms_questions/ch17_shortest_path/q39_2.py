"""
화성 탐사 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/26 16:06 ~ 16:16
# 정답!

import heapq

import sys
input = sys.stdin.readline

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(int(input())):
    n = int(input())

    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))

    INF = int(1e9)
    distance = [[INF] * n for _ in range(n)]
    distance[0][0] = graph[0][0]
    
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))

    while q:
        dist, r, c = heapq.heappop(q)

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
                heapq.heappush(q, (cost, nr, nc))

    print(distance[n-1][n-1])