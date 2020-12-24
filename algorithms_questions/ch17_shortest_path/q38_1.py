"""
정확한 순위 - 2회차
"""

# 풀이 제한 시간 : 40분
# 2020/12/24 10:17 ~ 10:22
# 정답

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = 0

for i in range(n):
    count = 0
    for j in range(n):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
    
    if count == n:
        answer += 1

print(answer)