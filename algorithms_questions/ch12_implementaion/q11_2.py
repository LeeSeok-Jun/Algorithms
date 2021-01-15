"""
뱀 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/15 13:08 ~ 13:44
# 정답!!!

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

n = int(input())
k = int(input())

data = [[0] * (n+2) for _ in range(n+2)]
data[1][1] = 1
for _ in range(k):
    r, c = map(int, input().split())
    data[r][c] = 2


l = int(input())
movement = []
for _ in range(l):
    x, c = input().split()
    movement.append((int(x), c))

snake = [(1, 1)]
head_r = 1
head_c = 1
direction = 0
time = 0

movement_index = 0
while True:
    time += 1

    head_r += dr[direction]
    head_c += dc[direction]

    if head_r <= 0 or head_r > n or head_c <= 0 or head_c > n:
        break

    if data[head_r][head_c] == 1:
        break
    elif data[head_r][head_c] == 2:
        data[head_r][head_c] = 1
        snake.append((head_r, head_c))
    else:
        data[head_r][head_c] = 1
        snake.append((head_r, head_c))
        tail_r, tail_c = snake.pop(0)
        data[tail_r][tail_c] = 0
        

    if movement_index < len(movement) and time == movement[movement_index][0]:
        if movement[movement_index][1] == 'L':
            direction -= 1
            direction %= 4
        else:
            direction += 1
            direction %= 4

        movement_index += 1

print(time)