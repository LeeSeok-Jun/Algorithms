"""
블록 이동하기
- https://programmers.co.kr/learn/courses/30/lessons/60063
"""

# 풀이 제한 시간 : 50분
# 2020/11/24 03:48 P.M. ~ 04:20 P.M.
# 실패 - BFS를 이용해야 된다는 개념은 알았지만 로봇을 어떻게 관리해야 할지 설계하지 못함

from collections import deque

def turn(robot, direction, n, board):
    partA, partB, state = robot

    # 시계방향
    if direction == 0:
        # 가로모드에서 세로모드로
        if state == 0:
            if partA[0] >= 2 and board[partA[0] - 1][partA[1]] != 1 and board[partB[0] - 1][partB[1]] != 1:
                return ((partA[0]-1, partA[1] + 1), partB, 1)
            else:
                return False
        # 세로모드에서 가로모드
        elif state == 1:
            if partA[1] < n and board[partA[0]][partA[1]+1] != 1 and board[partB[0]][partB[1]+1] != 1:
                return (partB, (partA[0]+1, partA[1]+1, 0))

def solution(board):
    answer = 0
    return answer