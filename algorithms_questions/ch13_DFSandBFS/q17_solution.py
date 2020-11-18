"""
경쟁적 전염 - 해설
"""

from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        if graph[i][j] != 0:
            # 바이러스 종류, 시간, 행, 열
            data.append((graph[i][j], 0, i, j))

data.sort()
q = deque(data)

s, x, y = map(int, input().split())

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while q:
    virus, t, r, c = q.popleft()
    if t == s:
        break

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < n and nc >=0 and nc < n:
            if graph[nr][nc] == 0:
                graph[nr][nc] = virus
                q.append((virus, t + 1, nr, nc))

print(graph[x-1][y-1])