"""
블록 이동하기 - 2회차
"""

# 풀이 제한 시간 : 50분
# 2020/12/01 12:21 ~ 13:00
# 실패

from collections import deque

def get_next(pos, new_board):

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    next_pos = []
    pos = list(pos)

    pos1_r, pos1_c, pos2_r, pos2_c = pos[0][0], pos[0][1], pos[1][0], pos[1][1]

    for i in range(4):
        next_pos1_r, next_pos1_c = pos1_r + dr[i], pos1_c + dc[i]
        next_pos2_r, next_pos2_c = pos2_r + dr[i], pos2_c + dc[i]

        # 움직여봤자 어차피 벽 안에서 움직이기 때문에 인덱스 범위 검사 필요 없다.
        """
        if 0 < next_pos1_r < n-1 and 0 < next_pos1_c < n-1 and 0 < next_pos2_r < n-1 and 0 < next_pos2_c < n-1:
            if new_board[next_pos1_r][next_pos1_c] == 0 and new_board[next_pos2_r][next_pos2_c] == 0:
                pass
        """
        if new_board[next_pos1_r][next_pos1_c] == 0 and new_board[next_pos2_r][next_pos2_c] == 0:
            next_pos.append({(next_pos1_r, next_pos1_c), (next_pos2_r, next_pos2_c)})


    if pos1_r == pos2_r:
        for i in [-1, 1]:
            # 움직여봤자 어차피 벽 안에서 움직이기 때문에 인덱스 범위 검사 필요 없다.
            """
            if 0 < pos1_r + i < n-1 and 0 < pos2_r + i < n-1:  
                if new_board[pos1_r + i][pos1_c] == 0 and new_board[pos2_r + i][pos2_c] == 0:
                    mode = 1
                    pass
            """
            if new_board[pos1_r + i][pos1_c] == 0 and new_board[pos2_r + i][pos2_c] == 0:
                next_pos.append({(pos1_r, pos1_c), (pos1_r + i, pos1_c)}) # pos1을 축으로 회전
                next_pos.append({(pos2_r, pos2_c), (pos2_r + i, pos2_c)}) # pos2를 축으로 회전

    elif pos1_c == pos2_c:
        for i in [-1, 1]:
            """
            if 0 < pos1_c + i < n-1 and 0 < pos2_c + i < n-1:  
                if new_board[pos2_r][pos1_c + i] == 0 and new_board[pos2_r][pos2_c + i] == 0:
                    mode = 0
                    pass
            """
            if new_board[pos1_r][pos1_c + i] == 0 and new_board[pos2_r][pos2_c + i] == 0:
                next_pos.append({(pos1_r, pos1_c), (pos1_r, pos1_c + i)}) # pos1을 축으로 회전
                next_pos.append({(pos2_r, pos2_c), (pos2_r, pos2_c + i)}) # pos2를 축으로 회전

    return next_pos


def solution(board):
    new_board = [[1] * len(board) + 2 for _ in range(len(board) + 2)]
    n = len(board)

    for i in range(len(board)):
        for j in range(len(board)):
            new_board[i+1][j+1] = board[i][j]

    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)}
    q.append((pos, 0))
    visited.append(pos)

    while q:
        pos, cost = q.popleft()

        if (n, n) in pos:
            return cost

        for next_pos in get_next(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost+1))
                visited.append(next_pos)

    return 0