"""
어른 상어 - 2회차
"""

# 풀이 제한 시간 : 50분
# 혼자 문제 풀어보면서 해결 방법이 생각 안 나는 부분은 기존 코드 참고

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

directions = list(map(int, input().split()))

smell = [[[0, 0]] * n for _ in range(n)]

priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def update_smell():
    for i in range(n):
        for j in range(n):
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

def move():
    new_array = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if array[r][c] != 0:
                direction = directions[array[r][c] - 1]
                found = False

                for index in range(4):
                    nr = r + dr[priorities[array[r][c] - 1][direction - 1][index] - 1]
                    nc = c + dc[priorities[array[r][c] - 1][direction - 1][index] - 1]

                    if nr >= 0 and nr < n and nc >= 0 and nc < n:
                        if smell[nr][nc][1] == 0:
                            directions[array[r][c] - 1] = priorities[array[r][c] - 1][direction - 1][index]

                            if new_array[nr][nc] == 0:
                                new_array[nr][nc] = array[r][c]
                            else:
                                new_array[nr][nc] = min(new_array[nr][nc], array[r][c])

                            found = True
                            break
                
                if found:
                    continue

                for index in range(4):
                    nr = r + dr[priorities[array[r][c] - 1][direction - 1][index] - 1]
                    nc = c + dc[priorities[array[r][c] - 1][direction - 1][index] - 1]

                    if nr >= 0 and nr < n and nc >= 0 and nc < n:
                        if smell[nr][nc][0] == array[r][c]:
                            directions[array[r][c]-1] = priorities[array[r][c] - 1][direction - 1][index]

                            new_array[nr][nc] = array[r][c]
                            break

    return new_array
            
time = 0

while True:
    update_smell()
    new_array = move()
    array = new_array
    time += 1

    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    if time > 1000:
        print(-1)
        break