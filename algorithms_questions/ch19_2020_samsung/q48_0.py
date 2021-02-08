"""
어른 상어
- https://www.acmicpc.net/problem/19237
"""

# 풀이 제한 시간 : 50분
# 2021/02/01 12:46 ~
# 실패 - 문제 코드 따라 해보면서 이해하기

import sys
input = sys.stdin.readline

# n : 격자의 크기 / m : 상어의 수 / k : 냄새가 사라지는 시간
n, m, k = map(int, input().split())

# 상어의 위차와 방향 저장
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 모든 상어의 현재 방향 정보 저장
directions = list(map(int, input().split()))

# 각 위치마다 [상어 번호, 냄새의 남은 시간]을 저장
smell = [[[0, 0]] * n for _ in range(n)]

# 각 상어의 회전 방향 우선순위 정보 저장
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 냄새 정보 업데이트
def update_smell():
    for i in range(n):
        for j in range(n):
            # 냄새가 남은 경우 시간을 1씩 감소
            # smell[i][j][0] : i행 j열의 상어 번호
            # smell[i][j][1] : i행 j열의 냄새가 남은 시간
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1

            # 상어가 있으면 해당 위치에 상어의 냄새 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]

# 모든 상어의 위치를 이동
def move():
    # 이동 결과를 담는 일시적인 테이블
    new_array = [[0] * n for _ in range(n)]

    for r in range(n):
        for c in range(n):
            if array[r][c] != 0:
                direction = directions[array[r][c] - 1] # 현재 상어의 방향
                found = False

                # 일단 냄새가 존재하는지 확인
                for index in range(4):
                    nr = r + dr[priorities[array[r][c] - 1][direction - 1][index] - 1]
                    nc = c + dc[priorities[array[r][c] - 1][direction - 1][index] - 1]

                    if nr >= 0 and nr < n and nc >= 0 and nc < n:
                        # 해당 위치에 냄새가 없으면 이동
                        if smell[nr][nc][1] == 0:
                            directions[array[r][c] - 1] = priorities[array[r][c] - 1][direction - 1][index]

                            if new_array[nr][nc] == 0:
                                new_array[nr][nc] = array[r][c]
                            else:
                                # 낮은 번호의 상어가 위치하도록 함
                                new_array[nr][nc] = min(new_array[nr][nc], array[r][c])
                            
                            found = True
                            break

                if found:
                    continue

                # 이동하지 못하고 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nr = r + dr[priorities[array[r][c] - 1][direction - 1][index] - 1]
                    nc = c + dc[priorities[array[r][c] - 1][direction - 1][index] - 1]

                    if nr >= 0 and nr < n and nc >= 0 and nc < n:
                        # 자신의 냄새가 있다면 이동
                        if smell[nr][nc][0] == array[r][c]:
                            directions[array[r][c] - 1] = priorities[array[r][c] - 1][direction - 1][index]

                            # 이동
                            new_array[nr][nc] = array[r][c]
                            break

    return new_array

time = 0

while True:
    update_smell()
    new_array = move()
    array = new_array
    time += 1

    # 1번 상어만 남았는지 검사
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False

    if check:
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
                