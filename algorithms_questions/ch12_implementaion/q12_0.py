"""
기둥과 보 설치
- https://programmers.co.kr/learn/courses/30/lessons/60061
- 기둥과 보를 이용하여 벽면 구조물을 자동으로 세우는 로봇을 개발할 계획인데, 그에 앞서 로봇의 동작을 시뮬레이션 할 수 있는 프로그램을 만들고 있다.
- 프로그램은 2차원 가상 벽면에 기둥과 보를 이용한 구조물을 설치할 수 있는데, 기둥과 보는 길이가 1인 선분으로 표현되며 다음과 같은 규칙을 가지고 있다.
    * 기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 한다.
    * 보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 한다.
- 단, 바닥은 벽면의 맨 아래 지면을 말한다.
- 2차원 벽면은 n x n 크기 정사각 격자 형태이며, 각 격자는 1 x 1 크기이다.
- 맨 처음 벽면은 비어있는 상태이다. 기둥과 보는 격자선의 교차점에 걸치지 않고, 격자 칸의 각 변에 정확히 일치하도록 설치할 수 있다.
- 둥과 보를 삭제하는 기능도 있는데 기둥과 보를 삭제한 후에 남은 기둥과 보들 또한 위 규칙을 만족해야 한다.
  만약, 작업을 수행한 결과가 조건을 만족하지 않는다면 해당 작업은 무시된다.
- 벽면의 크기 n, 기둥과 보를 설치하거나 삭제하는 작업이 순서대로 담긴 2차원 배열 build_frame이 매개변수로 주어질 때,
  모든 명령어를 수행한 후 구조물의 상태를 return 하도록 solution 함수를 완성하라.
"""

# 2020/11/09 01:19 P.M. ~ 02:26 P.M.
# 실패

# [x, y, a, b]
# x, y : 좌표
# a => 0 : 기둥 / 1 : 보
# b => 0 : 삭제 / 1 : 설치
# 기둥은 위로, 보는 오른쪽으로만 설치 가능

def solution(n, build_frame):
    board = [[-1] * (n+1) for _ in range(n+1)]

    for frame in build_frame:
        x = frame[0] # x좌표
        y = frame[1] # y좌표
        a = frame[2] # 기둥 or 보
        b = frame[3] # 설치 or 삭제

        # 설치
        if b == 1:
            if a == 0:
                if IsConditionPilar(x, n-y, board):
                    board[n-y][x] = 0
            else:
                if IsConditionBo(x, n-y, board):
                    board[n-y][x] = 1
        # 삭제
        else:
            if a == 0:
                if IsConditionPilar(x, n-y, board) or IsConditionBo(x, n-y, board):
                    board[n-y][x] = -1

    answer = []

    for i in range(n+1):
        for j in range(n+1):
            if board[n-i][j] != -1:
                answer.append([j, i, board[n-i][j]])

    import pprint
    pprint.pprint(board)

    return sorted(answer)

def IsConditionPilar(x, ny, board):
    if board[ny][x] == -1:
        if ny == len(board) - 1:
            return True
        elif board[ny+1][x] == 0:
            return True
        elif board[ny][x-1] == 1 or board[ny][x+1] == 1:
            return True
        else:
            return False
    return False

def IsConditionBo(x, ny, board):
    if board[ny][x] == -1:
        if board[ny+1][x] == 0 or board[ny+1][x+1] == 0:
            return True
        elif board[ny][x-1] == 1 and board[ny][x+1] == 1:
            return True
        else:
            return False
    return False


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))