"""
아기 상어 - 2회차
"""

# 풀이 제한 시간 : 50분
# 혼자 문제 풀어보면서 해결 방법이 생각 안 나는 부분은 기존 코드 참고

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

# 현재 상어의 위치를 찾고 공란으로 설정
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_r, now_c = i, j
            array[i][j] = 0

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 현재 상어에서 먹을 수 있거나 지나갈 수 있는 물고기의 최소 거리를 저장
def bfs():
    # 최소 거리를 저장하는 테이블
    dist = [[-1] * n for _ in range(n)]

    q = deque([now_r, now_c])
    dist[now_r][now_c] = 0

    while q:
        r, c = q.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr > 0 and nr < n and nc >= 0 and nc < n:
                # 사이즈가 같으면 먹을 순 없지만, 지나갈 수는 있다.
                if dist[nr][nc] == -1 and array[nr][nc] <= now_size:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    return dist

# 현재 상어의 위치에서 가장 가까이 위치한 먹을 수 있는 물고기를 찾음
def find(dist):
    r, c = 0, 0
    min_dist = INF

    for i in range(n):
        for j in range(n):
            # 먹을 수 있는 물고기만 찾기 때문에 < 부등호 사용
            if dist[i][j] != -1 and array[i][j] >= 1 and array[i][j] < now_size:
                if dist[i][j] < min_dist:
                    r, c = i, j # 먹을 수 있는 가장 가까운 물고기의 위치
                    min_dist = dist[i][j] # 먹을 수 있는 가장 가까운 물고기까지의 거리

    # 최소 거리가 무한대이면 먹을 수 있는 물고기가 없음을 의미
    if min_dist == INF:
        return None

    # 먹을 수 있는 물고기의 위치와 거리를 반환
    else:
        return r, c, min_dist


result = 0
ate = 0

while True:
    value = find(bfs())

    # 더 이상 먹을 수 있는 물고기가 없으면 종료
    if value == None:
        print(result)
        break

    else:
        # 해당 물고기의 위치로 상어를 이동
        now_r, now_c = value[0], value[1]
        result += value[2] # 해당 물고기까지의 거리를 추가(거리 = 시간)

        array[now_r][now_c] = 0
        ate += 1

        # 자신의 현재 크기만큼 물고기를 먹었으면 사이즈 증가
        if ate >= now_size:
            now_size += 1
            ate = 0