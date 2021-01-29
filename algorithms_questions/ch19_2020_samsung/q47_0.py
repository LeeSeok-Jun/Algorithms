"""
청소년 상어
- https://www.acmicpc.net/problem/19236
"""

# 풀이 제한 시간 : 50분
# 2021/01/29 13:50 ~ 15:13
# 실패 - 코드 이해하기

import copy
import sys
input = sys.stdin.readline

graph = [[None] * 4 for _ in range(4)]

# 문제 입력
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        # 방향 인덱스 통일을 위해 입력에서 1을 감소시킴
        # graph[i][j][0] = 물고기 번호
        # graph[i][j][1] = 물고기 방향
        graph[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

# 8가지 방향 정의
# 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

# 현재 위치에서 반시계 방향으로 회전하는 함수
def turn_left(direction):
    return (direction + 1) % 8

result = 0

# 현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(graph, index):
    for i in range(4):
        for j in range(4):
            if graph[i][j][0] == index:
                return (i, j)

    return None

# 모든 물고기들을 회전 및 이동시키는 함수
def move_all_fishes(graph, now_r, now_c):
    # 1번부터 16번 물고기를 차례로 확인
    for i in range(1, 17):
        # 현재 물고기의 위치 찾음
        position = find_fish(graph, i)

        if position != None:
            r, c = position[0], position[1]
            direction = graph[r][c][1]

            # 해당 물고기를 방향을 왼쪽으로 회전시키며 이동이 가능한지 확인
            for _ in range(8):
                nr = r + dr[direction]
                nc = c + dc[direction]

                # 이동 가능하면 이동 시키기
                if nr >= 0 and nr < 4 and nc >= 0 and nc < 4:
                    if not(nr == now_r and nc == now_c):
                        graph[r][c][1] = direction
                        # 물고기 위치 교환
                        graph[r][c], graph[nr][nc] = graph[nr][nc], graph[r][c]
                        break

                # 이동 불가능하면 회전
                direction = turn_left(direction)

# 상어가 현재 위치에서 먹을 수 있는 모든 물고기의 위치 반환
def get_possible_positions(graph, now_r, now_c):
    positions = []
    direction = graph[now_r][now_c][1]

    # 현재 방향으로 계속 이동
    # 방향은 유지한 채 최대 4번 이동
    for _ in range(4):
        now_r += dr[direction]
        now_c += dc[direction]

        # 범위를 벗어나지 않는지 확인
        if now_r >= 0 and now_r < 4 and now_c >= 0 and now_c < 4:
            # 물고기가 존재하는지 확인
            if graph[now_r][now_c][0] != -1:
                # 존재할 경우 해당 물고기의 위치 저장
                positions.append((now_r, now_c))

    return positions

# DFS
def dfs(graph, now_r, now_c, total):
    global result
    graph = copy.deepcopy(graph)

    # 현재 위치의 물고기 먹기
    total += graph[now_r][now_c][0]
    graph[now_r][now_c][0] = -1 # 물고기를 먹었으므로 번호를 -1로 표시

    move_all_fishes(graph, now_r, now_c) # 모든 물고기 이동

    # 상어 위치 이동
    positions = get_possible_positions(graph, now_r, now_c)

    # 이동 불가능하면 정지
    if len(positions) == 0:
        result = max(result, total) # 최댓값 저장
        return

    # 이동 가능하면 재귀적 수행
    for next_r, next_c in positions:
        dfs(graph, next_r, next_c, total)

# 시작 위치인 (0, 0)에서 재귀적으로 모든 경우 탐색
dfs(graph, 0, 0, 0)
print(result)
