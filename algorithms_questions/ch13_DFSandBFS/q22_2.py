"""
블록 이동하기 - 3회차
"""

# 풀이 제한 시간 : 50분
# 2021/01/20 13:47 ~ 14:43
# 실패 - 틀린 부분 주석 처리
# 집합 자료형 사용

from collections import deque


def nextPosition(robot, new_board):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    # queue = deque()
    # queue.append((r1, c1, r2, c2))

    # while queue:
    #     now_r1, now_c1, now_r2, now_c2 = queue.popleft()

    # 내가 생각하지 못한 부분
    next_robot = []
    robot = list(robot)

    now_r1, now_c1, now_r2, now_c2 = robot[0][0], robot[0][1], robot[1][0], robot[1][1]

    # 이동
    for i in range(4):
        next_r1, next_c1, next_r2, next_c2 = now_r1 + dr[i], now_c1 + dc[i], now_r2 + dr[i], now_c2 + dc[i]
        
        # 인덱스 범위 검사 불필요
        #  if 0 < next_r1 < n and 0 < next_c1 < n and 0 < next_r2 < n and 0 < next_c2 < n:
        
        if new_board[next_r1][next_c1] == 0 and new_board[next_r2][next_c2] == 0:
            # queue.append((next_r1, next_c1, next_r2, next_c2))
            next_robot.append({(next_r1, next_c1), (next_r2, next_c2)})

    # 회전(가로 -> 세로)
    if now_r1 == now_r2:
        for i in [-1, 1]:
            if new_board[now_r1 + i][now_c1] == 0 and new_board[now_r2 + i][now_c2] == 0:
                next_robot.append({(now_r1, now_c1), (now_r1 + i, now_c1)})
                next_robot.append({(now_r2, now_c2), (now_r2 + i, now_c2)})

    elif now_c1 == now_c2:
        for i in [-1, 1]:
            if new_board[now_r1][now_c1 + i] == 0 and new_board[now_r2][now_c2 + i] == 0:
                next_robot.append({(now_r1, now_c1), (now_r1, now_c1 + i)})
                next_robot.append({(now_r2, now_c2), (now_r2, now_c2 + i)})

    return next_robot
                

def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]

    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]

    q = deque()
    visited = []
    robot = {(1, 1), (1, 2)}
    q.append((robot, 0))
    visited.append(robot)

    while q:
        robot, time = q.popleft()

        if (n, n) in robot:
            return time

        for next_robot in nextPosition(robot, new_board):
            if next_robot not in visited:
                q.append((next_robot, time + 1))
                visited.append(next_robot)

    return 0