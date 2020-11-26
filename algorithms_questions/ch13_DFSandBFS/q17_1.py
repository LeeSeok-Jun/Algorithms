"""
경쟁적 전염 - 2회차
"""

# 풀이 제한 시간 : 50분
# 2020/11/26 12:10 ~ 12:33
# 컴파일 시간 초과
# 바이러스의 종류, '시간', 행, 열을 저장한다!

from collections import deque

n, k = map(int, input().split())

graph = []

q = deque()

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    for j in range(n):
        if graph[i][j] != 0:
            q.append((graph[i][j], i, j))

s, x, y = map(int, input().split())

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def virus(number, r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            if graph[nr][nc] == 0:
                graph[nr][nc] = number

t = 0
while(t < s):
    q = sorted(q)

    while q:
        number, r, c = q.pop(0)
        virus(number, r, c)

    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                q.append((graph[i][j], i, j))

    t += 1


print(graph[x-1][y-1])