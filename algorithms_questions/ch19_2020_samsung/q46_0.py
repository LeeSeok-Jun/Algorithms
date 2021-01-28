"""
아기 상어
- https://www.acmicpc.net/problem/16236
"""

# 풀이 제한 시간 : 50분
# 2021/01/28 14:20 ~
# 실패
# BFS를 응용하기!

# n = int(input())

# data = []
# fish = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
#     for j in range(n):
#         if data[i][j] == 9:
#             shark = (2, i ,j)

#         elif data[i][j] in [1, 2, 3, 4 ,5, 6]:
#             fish.append(data[i][j], i, j)

# fish.sort()

from collections import deque
import sys
input = sys.stdin.readline

INF = int(1e9)
n = int(input())

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

now_size = 2
now_r, now_c = 0, 0

for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_r, now_c = i, j
            array[now_r][now_c] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 현재 상어의 위치에서 먹을 수 있는 각각의 물고기에 대한 최소 거리를 구함
def bfs():
    dist = [[-1] * n for _ in range(n)] # 거리 정보를 저장하는 2차원 배열
    # 함수 연산이 끝난 뒤 값이 -1이면 도달할 수 없다는 것을 의미 

    q = deque([(now_r, now_c)])
    dist[now_r][now_c] = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                if dist[nr][nc] == -1 and array[nr][nc] <= now_size:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    # 계산된 거리 정보를 반환한다.
    return dist

# 현재 상어의 위치에서 가장 가까운 위치에 있는 먹을 수 있는 물고기를 찾음
# 이 함수는 bfs를 통해 연산된 dist를 이용하여 연산한다.
def find(dist):
    r, c = 0, 0
    min_dist = INF

    for i in range(n):
        for j in range(n):
            if dist[i][j] != -1 and array[i][j] >= 1 and array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    r, c = i, j
                    min_dist = dist[i][j]

    # 먹을 수 있는 물고기가 없는 경우
    if min_dist == INF:
        return None

    # 먹을 수 있는 물고기가 있는 경우 해당 물고기의 좌표와 최소 거리 반환
    else:
        return r, c, min_dist

result = 0 # 출력 결과
ate = 0 # 먹은 물고기의 수

while True:
    value = find(bfs()) # 가장 가까운 위치에 있는 물고기 정보를 가져옴

    # 더 이상 먹을 수 있는 물고기가 없는 경우 종류
    if value == None:
        print(result)
        break

    else:
        # 해당 물고기를 먹고 상어를 그 위치로 이동
        now_r, now_c = value[0], value[1]
        result += value[2]

        array[now_r][now_c] = 0
        ate += 1

        # 상어의 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0