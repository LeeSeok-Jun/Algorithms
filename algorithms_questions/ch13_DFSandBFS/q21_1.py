"""
인구 이동 - 2회차
"""

# 풀이 제한 시간 : 40분
# 2020/12/01 11:34 ~ 12:10
# 실패 - bfs를 이용해야 함


n, min_value, max_value = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

answer = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

"""
now = 1
union = [[0] * n for _ in range(n)]
num_of_union = [1] * ((n+1) * (n+1))

def makeUnion(r, c, now):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < n and nc >= 0 and nc < n:
            if union[nr][nc] == 0:
                if abs(graph[r][c] - graph[nr][nc]) >= min_value and abs(graph[r][c] - graph[nr][nc]) <= max_value:
                    union[nr][nc] = now
                    num_of_union[now] += 1

                    makeUnion(nr, nc, now)

def move():        
    for r in range(n):
        for c in range(n):
            if union[r][c] == 0:
                union[r][c] = now
                makeUnion(r, c, now)
                now += 1

    for r in range(n):
        for c in range(c):
            if union[r][c] != 0:
                graph[r][c] = int(union[r][c] / num_of_union[union[r][c]])
"""

from collections import deque # 큐 자료구조 사용을 위한 모듈 선언

def bfs(r, c, index):
    united = []
    united.append((r, c))

    queue = deque()
    queue.append((r, c))

    union[r][c] = index
    summary = graph[r][c]
    count = 1

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and union[nr][nc] == -1:
                if min_value <= abs(graph[r][c] - graph[nr][nc]) <= max_value:
                    queue.append((nr, nc))

                    union[nr][nc] = index
                    summary += graph[nr][nc]
                    count += 1
                    united.append((nr, nc))

    for r, c in united:
        graph[r][c] = summary // count

    return count

while True:
    union = [[-1] * n for _ in range(4)]
    index = 0

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1

    if index == n * n:
        break

    answer += 1

print(answer)