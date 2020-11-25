"""
연구소 - 2회차
"""

# 풀이 제한 시간 : 40분
# 2020/11/25 12:45 P.M. ~ 01:12 P.M.
# 성공 - 함수 반환하고 인덱스 범위 꼼꼼하게 살피기

n, m = map(int, input().split())

graph = []
temp = [[0] * m for _ in range(n)]

for i in range(n):
    graph.append(list(map(int, input().split())))


answer = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def virus(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        # 인덱스가 0보다 크거나 같음!!!
        if nr >= 0 and nr < n and nc >= 0 and nc < m:
            if temp[nr][nc] == 0:
                temp[nr][nc] = 2
                virus(nr, nc)

def getAnswer():
    count = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                count += 1
    
    return count

def dfs(count):
    global answer

    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        answer = max(answer, getAnswer())
        return # 빠뜨린 부분
    
    else:
        for i in range(n):
            for j in range(m):
                if graph[i][j] == 0:
                    graph[i][j] = 1
                    count += 1
                    
                    dfs(count)

                    graph[i][j] = 0
                    count -= 1

dfs(0)
print(answer)

