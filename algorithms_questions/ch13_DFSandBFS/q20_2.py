"""
감시 피하기 - 3회차
"""

# 풀이 제한 시간 : 60분
# 2021/01/19 14:08 ~ 14:33
# 정답!

import sys
input = sys.stdin.readline

n = int(input())

graph = []
num_teacher = 0
for i in range(n):
    graph.append(input().split())

    for j in range(n):
        if graph[i][j] == 'T':
            num_teacher += 1

answer = 'NO'

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def seachStudent(r, c):
    for i in range(4):
        nr = r
        nc = c

        while True:
            nr += dr[i]
            nc += dc[i]

            if nr < 0 or nr >= n or nc < 0 or nc >= n or graph[nr][nc] == 'O':
                break

            if graph[nr][nc] == 'S':
                return False
    
    return True

def dfs(count):
    global answer

    if count == 3:
        safe = 0
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T':
                    if seachStudent(i, j):
                        safe += 1

        if num_teacher == safe:
            answer = 'YES'

    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    count += 1

                    dfs(count)

                    graph[i][j] = 'X'
                    count -= 1

dfs(0)
print(answer)
