"""
미로 탈출
- 어떤 사람이 N * M 크기의 직사각형 형태의 미로에 갇혀 있다.
- 미로에는 괴물이 있어 이를 피해 탈출해야 한다.
- 사람의 위치는 (1, 1)이고 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동할 수 있다.
- 이 때, 괴물이 있는 부분은 0, 괴물이 없는 부분은 1로 표시한다.
- 미로는 반드시 탈출할 수 있는 형태로 제시된다.
- 이때 사람이 미로를 탈출하기 위해 움직여야 하는 최소 칸의 개수를 구하시오.
- 칸을 셀 때는 시작 칸(출발)과 마지막 칸(출구)을 모두 포함해서 계산한다.

입력 조건
- 첫째 줄에 두 정수 N, M(4 <= N, M <= 200)이 주어진다.
- 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어진다.
- 각각의 수들은 공백 없이 붙어서 입력으로 제시된다. 또한, 시작 칸과 마지막 칸은 항상 1이다.

출력 조건
- 첫째 줄에 최소 이동 칸의 개수를 출력한다.
"""

from collections import deque

# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0] # 행 이동
dy = [0, 0, -1, 1] # 열 이동

# BFS 구현
def bfs(x, y):
    # 큐 생성
    queue = deque()
    queue.append((x, y))

    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 이동 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 공간 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 괴물이 있는 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래(출구)까지의 최단 거리 반환
    return graph[n - 1][m - 1]

print(bfs(0, 0))