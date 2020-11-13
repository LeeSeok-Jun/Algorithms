"""
뱀 - 2회차
"""

# 2020/11/13 10:17 A.M. ~ 10:52 A.M.
# 정답!

n = int(input())

board = [[0] * (n + 1) for _ in range(n+1)]

k = int(input())

for _ in range(k):
    r, c = map(int, input().split())
    board[r][c] = 2

l = int(input())

moving = []
for _ in range(l):
    x, c = input().split()
    moving.append((int(x), c))

snake = []
head_r = 1
head_c = 1
snake.append((head_r, head_c))
board[head_r][head_c] = 1
direction = 0

def move(direction, head_r, head_c):
    # R, D, L, U
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    return head_r + dr[direction], head_c + dc[direction]

sec = 1
i = 0
while(True):
    head_r, head_c = move(direction, head_r, head_c)

    if head_r >= len(board) or head_c >= len(board) or head_r <= 0 or head_c <= 0:
        break
    
    if board[head_r][head_c] == 1:
        break
    elif board[head_r][head_c] == 0:
        board[head_r][head_c] = 1
        snake.append((head_r, head_c))

        board[snake[0][0]][snake[0][1]] = 0
        snake.pop(0)
    elif board[head_r][head_c] == 2:
        board[head_r][head_c] = 1
        snake.append((head_r, head_c))

    if i < len(moving) and sec == moving[i][0]:
        if moving[i][1] == 'L':
            direction -= 1
            if direction < 0:
                direction = 4
            i += 1
        elif moving[i][1] == 'D':
            direction = (direction + 1) % 4
            i += 1
    
    sec += 1

print(sec)


