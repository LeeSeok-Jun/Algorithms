from collections import deque

def get_next_pos(pos, board):
    next_pos = [] # 이동 가능한 위치들
    pos = list(pos) # 현재 위치 정보를 집합 자료형에서 리스트 자료형으로 형변환

    pos1_r, pos1_c, pos2_r, pos2_c = pos[0][0], pos[0][1], pos[1][0], pos[1][1] # 로봇의 위치

    # 상,하,좌,우 이동에 대한 처리
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for i in range(4):
        pos1_next_r, pos1_next_c, pos2_next_r, pos2_next_c = pos1_r + dr[i], pos1_c + dc[i], pos2_r + dr[i], pos2_c + dc[i]

        # 이동 가능한 경우
        if board[pos1_next_r][pos1_next_c] == 0 and board[pos2_next_r][pos2_next_c] == 0:
            next_pos.append({(pos1_next_r, pos1_next_c), (pos2_next_r, pos2_next_c)}) # 이동 가능한 위치에 집합 자료형 형태로 추가

    # 회전에 대한 처리
    # 가로 모드일 경우
    if pos1_r == pos2_r:
        # 위로 회전(-1)과 아래로 회전(+1)에 대해
        for i in [-1, 1]:
            # 위, 아래로 모두 빈 공간이면 회전 가능
            if board[pos1_r + i][pos1_c] == 0 and board[pos2_r + i][pos2_c] == 0:
                next_pos.append({(pos1_r, pos1_c), (pos1_r + i, pos1_c)}) # pos1을 축으로 회전
                next_pos.append({(pos2_r, pos2_c), (pos2_r + i, pos2_c)}) # pos2를 축으로 회전

    # 세로 모드일 경우
    elif pos1_c == pos2_c:
        # 왼쪽 회전(-1)과 오른쪽 회전(+1)에 대해
        for i in [-1, 1]:
            # 좌, 우 모두 빈 공간이면 회전 가능
            if board[pos1_r][pos1_c + i] == 0 and board[pos2_r][pos2_c + i] == 0:
                next_pos.append({(pos1_r, pos1_c), (pos1_r, pos1_c + i)}) # pos1을 축으로 회전
                next_pos.append({(pos2_r, pos2_c), (pos2_r, pos2_c + i)}) # pos2를 축으로 회전

    return next_pos # 현재 위치에서 이동 가능한 위치 반환

def solution(board):
    # 맵의 외곽에 벽을 새롭게 만듦
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]

    # BFS 수행
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치
    q.append((pos, 0)) # 위치 정보와 탐색 시간을 큐에 삽입
    visited.append(pos) # 방문 처리

    while q:
        pos, cost = q.popleft()

        if (n, n) in pos:
            return cost
        
        for next_pos in get_next_pos(pos, new_board):
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)

    return 0