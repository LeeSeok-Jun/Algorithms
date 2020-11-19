"""
감시 피하기
- https://www.acmicpc.net/problem/18428
"""

# 풀이 제한 시간 : 60분
# 2020/11/19 12:17 P.M. ~ 13:10 P.M.
# 정답!

n = int(input())

graph = []
temp = [[0] * n for _ in range(n)]
teacher = 0
possible = 0
result = "NO"

for i in range(n):
    graph.append(input().split())

    for j in range(n):
        if graph[i][j] == 'T':
            teacher += 1

dr = [-1, 0, 1, 0] # 상하 이동
dc = [0, 1, 0, -1] # 좌우 이동

def watch(r, c):
    for i in range(4):
        nr = r
        nc = c
        while True:
            nr += dr[i]
            nc += dc[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                if temp[nr][nc] == 'S':
                    return False
                elif temp[nr][nc] == 'O':
                    break
            else:
                break
        
    return True

def dfs(count):
    global result

    if count == 3:
        possible = 0

        for i in range(n):
            for j in range(n):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(n):
                if temp[i][j] == 'T':
                    if watch(i, j):
                        possible += 1

        if possible == teacher:
            result = "YES"
        
        return

    for i in range(n):
        for j in range(n):
            if graph[i][j] == 'X':
                graph[i][j] = 'O'
                count += 1

                dfs(count)

                graph[i][j] = 'X'
                count -= 1
                
dfs(0)
print(result)