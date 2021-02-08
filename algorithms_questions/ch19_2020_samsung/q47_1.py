"""
청소년 상어 - 2회차
"""

# 풀이 제한 시간 : 50분
# 혼자 문제 풀어보면서 해결 방법이 생각 안 나는 부분은 기존 코드 참고

import copy
import sys
input = sys.stdin.readline

array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))

    for j in range(4):
        array[i][j] = [data[j * 2], data[j * 2 + 1] - 1]

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]

def turn_left(direction):
    return (direction + 1) % 8

result = 0

# 물고기 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i, j)

    return None


# 물고기 이동
# now_r, now_c : 상어 위치
def move_all_fishes(array, now_r, now_c):
    for i in range(1, 17):
        position = find_fish(array, i)

        if position != None:
            r, c = position[0], position[1]
            direction = array[r][c][1]

            # 최대 8번까지 회전
            for _ in range(8):
                nr = r + dr[direction]
                nc = c + dc[direction]

                if nr >= 0 and nr < 4 and nc >= 0 and nc < 4:
                    if not(nr == now_r and nc == now_c):
                        array[r][c][1] = direction
                        array[r][c], array[nr][nc] = array[nr][nc], array[r][c]

                        break
            
                    
                direction = turn_left(direction)


# 상어가 먹을 수 있는 모든 물기 위치 확인
def get_possible_positions(array, now_r, now_c):
    positions = []
    direction = array[now_r][now_c][1]

    # 최대 한 방향으로 4번까지 이동
    for _ in range(4):
        now_r += dr[direction]
        now_c += dc[direction]

        if now_r >= 0 and now_r < 4 and now_c >= 0 and now_c < 4:
            if array[now_r][now_c][0] != -1:
                positions.append((now_r, now_c))


    return positions


# dfs로 재귀적으로 물고기 먹기
def dfs(array, now_r, now_c, total):
    global result
    array = copy.deepcopy(array)

    total += array[now_r][now_c][0]
    array[now_r][now_c][0] = -1 # 상어 위치

    # 물고기 이동
    move_all_fishes(array, now_r, now_c)

    # 상어 이동
    positions = get_possible_positions(array, now_r, now_c)

    if len(positions) == 0:
        result = max(result, total)
        return

    for next_r, next_c in positions:
        dfs(array, next_r, next_c, total)

dfs(array, 0, 0, 0)
print(result)