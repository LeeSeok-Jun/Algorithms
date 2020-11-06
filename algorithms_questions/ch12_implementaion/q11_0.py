"""
뱀
- 게임은 N * N 정사각 보드 위에서 진행되고 몇몇 칸에는 사과가 존재한다.
- 보드의 상하좌우 끝에는 벽이 존재한다.
- 게임을 시작할 때 뱀은 맨 위 좌측에 위치하고 뱀의 길이는 1이다.
- 뱀은 맨 처음 오른쪽을 향하며 매 초마다 다음과 같은 규칙을 따른다.
    * 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    * 만약 이동한 칸에 사과가 있다면 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    * 만약 이동한 칸에 사과가 없다면 몸 길이를 줄여서 꼬리가 위치한 칸을 비운다.
      즉, 몸길이는 변하지 않는다.
- 사과의 위치와 뱀의 이동 경로가 주어질 때 이 게임이 몇 초에 끝나는지 계산하시오.

입력 조건
- 첫째 줄에 보드의 크기 N이 주어진다.(2 <= N <= 100) 다음 줄에 사과의 개수 K가 주어진다.(0 <= K <= 100)
- 다음 K개의 줄에는 사과의 위치가 주어지는데, 첫 번째 정수는 행, 두 번째 정수는 열 위치를 의미한다.
    * 사과의 위치는 모두 다르며, 맨 위 좌측(1행 1열)에는 사과가 없다.
- 다음 줄에는 뱀의 방향 전환 횟수 L이 주어진다. (1 <= L <= 100)
- 다음 L개의 줄에는 뱀의 방향 전환 정보가 주어지는데, 정수 X와 문자 C로 이루어져있다.
    * 게임 시작 시간으로부터 X초가 끝난 뒤에는 C방향으로 90도 회전시킨다는 의미이다.
    * X는 10,000이하의 양의 정수이며, 방향 전환 정보는 X가 증가하는 순으로 주어진다.

출력 조건
- 첫째 줄에 게임이 몇 초만에 끝나는지 출력한다.
"""

# https://www.acmicpc.net/problem/3190

# 2020/11/06 11:08 A.M. ~ 시간 초과

# 1. 행렬에서의 이동에 대해서 정확하게 생각하기
#   * 좌우 이동 = 열 변환
#   * 상하 이동 = 행 변환

# 2. 뱀의 위치정보를 리스트로 저장하면, 꼬리를 쉽게 삭제할 수 있다.

# 3. 배열의 인덱스에 대해 꼼꼼하게 살피기!
#   * 배열을 검사 할 경우 먼저 검사하려는 인덱스가 배열의 크기를 벗어나는지 여부를 사전에 검사해야한다.

n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수

# 보드 생성
board = [[0] * (n + 1) for _ in range(n+1)]
# borad[a][b]에 대해서
# 0 : 빈 공간
# 1 : 뱀의 위치
# 2 : 사과의 위치

# 사과 위치 설정
for i in range(k):
    r, c = map(int, input().split())
    board[r][c] = 2

l = int(input()) # 뱀의 방향 변화 횟수

# 뱀의 방향 젼환 설정
will = []
for j in range(l):
    x, c = input().split()
    will.append((int(x), c))

# 뱀의 현재 위치
head_r = 1
head_c = 1
board[head_r][head_c] = 1
snake = [(head_r, head_c)] # 뱀의 위치 정보를 저장

# 뱀의 머리 방향
ahead = ['R', 'D', 'L', 'U']
now = 0

def turn(direction, now):
    if direction == 'L':
        now -= 1
        if now < 0:
            now = 3
    else:
        now += 1
        if now > 3:
            now = 0

    return now

def move(head_r, head_c, ahead, now):
    if ahead[now] == 'R':
        head_c += 1
    elif ahead[now] == 'D':
        head_r += 1
    elif ahead[now] == 'L':
        head_c -= 1
    else:
        head_r -= 1

    return head_r, head_c

count = 0
will_index = 0
while(True):
    count += 1 # 1초 증가 후
    head_r, head_c = move(head_r, head_c, ahead, now) # 움직임 진행

    # 먼저 뱀이 보드를 벗어나면 종료
    if head_r <= 0 or head_r > n or head_c <= 0 or head_c > n:
        break

    # 뱀이 사과를 만났을 때
    if board[head_r][head_c] == 2:
        board[head_r][head_c] -= 1
        snake.append((head_r, head_c)) # 이동된 머리 정보를 리스트에 저장
    # 사과를 만나지 못했을 때
    elif board[head_r][head_c] == 0:
        board[head_r][head_c] += 1
        snake.append((head_r, head_c)) # 이동된 머리 정보를 리스트에 저장
        tail_r, tail_c = snake.pop(0) # 리스트의 가장 첫번째 원소(= 꼬리)를 꺼냄
        board[tail_r][tail_c] -= 1 # 해당 자리의 값을 0으로
    # 자기 몸통을 만났을 때
    elif board[head_r][head_c] == 1:
        break # 반복 종료

    # 방향전환이 발생하는 시간이 되면 방향전환 진행
    # 이때 방향 전환 정보를 담고 있는 배열의 인덱스 초과를 주의해야 한다!
    if will_index < l and count == will[will_index][0]:
        direction = will[will_index][1]
        now = turn(direction, now)
        will_index += 1

print(count)
