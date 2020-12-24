"""
플로이드 - 2회차
"""

# 풀이 제한 시간 : 40분
# 2020/12/24 10:05 ~ 10:14
# 정답

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
    if c < graph[a-1][b-1]:
        graph[a-1][b-1] = c

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

