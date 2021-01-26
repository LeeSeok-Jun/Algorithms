"""
플로이드 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/26 15:26 ~ 15:36
# 정답!

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a-1][b-1] = min(c, graph[a-1][b-1])

for k in range(n):
    for r in range(n):
        for c in range(n):
            graph[r][c] = min(graph[r][c], graph[r][k]+graph[k][c])

for r in range(n):
    for c in range(n):
        if graph[r][c] == INF:
            print(0, end=" ")
        else:
            print(graph[r][c], end=" ")

    print()