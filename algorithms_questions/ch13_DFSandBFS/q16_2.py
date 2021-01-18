"""
연구소 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/18 14:53 ~ 15:40
# 실패 - 틀린 부분 주석 처리

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

graph = []
temp = [[0] * (m) for _ in range(n)]

answer = 0

for i in range(n):
    graph.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def virusMove(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # nr >= 0 or nr < n or nc >= 0 or nc < m:
        if nr >= 0 and nr < n and nc >= 0 and nc < m:
            if temp[nr][nc] == 0:
                temp[nr][nc] = 2
                virusMove(nr, nc)

def getAnswer():
    check = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                check += 1

    return check


def dfs(count):
    global answer

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virusMove(i, j)

        answer = max(answer, getAnswer())
        return

    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    count += 1

                    dfs(count)

                    graph[i][j] = 0
                    count -= 1 # 빼먹음

dfs(0)
print(answer)
