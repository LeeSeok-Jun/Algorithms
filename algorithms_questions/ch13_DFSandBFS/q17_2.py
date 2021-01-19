"""
경쟁적 전염 - 3회차
"""

# 풀이 제한 시간 : 50분
# 2021/01/19 12:36 ~ 13:05
# 정답!

import sys
input = sys.stdin.readline

import heapq

n, k = map(int, input().split())

graph = []
q = []
for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        if graph[i][j] != 0:
          heapq.heappush(q, (0, graph[i][j], i, j))

s, x, y = map(int, input().split())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def virus(t, k, r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            if graph[nr][nc] == 0:
                graph[nr][nc] = k
                heapq.heappush(q, (t+1, k, nr, nc))
            else:
                continue

while q:
    now_t, now_k, now_r, now_c = heapq.heappop(q)

    if now_t >= s:
        break

    virus(now_t, now_k, now_r, now_c)

print(graph[x-1][y-1])



