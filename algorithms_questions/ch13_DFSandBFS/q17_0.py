"""
경쟁적 전염
- https://www.acmicpc.net/problem/18405
- N * N 크기의 시험관은 1 * 1 크기의 칸으로 나뉘어짔으며 특정 위치에는 바이러스가 존재할 수 있다.
- 바이러스의 종류는 1부터 K번까지 총 K가지가 있으며 모든 바이러스는 이 중 하나에 속한다.
- 시험관에 존재하는 바이러스는 1초마다 상, 하, 좌, 우로 증식하는데, 매 초마다 번호가 작은 바이러스 부터 증식한다.
- 특정 위치에 이미 바이러스가 존재한다면 다른 바이러스들은 그 곳에 증식할 수 없다.
- 시험관의 크기와 바이러스의 위치 정보가 주어졌을 때, S초가 지난 뒤에 (X, Y)에 존재하는 바이러스의 종류를 출력하는 프로그램을 작성하시오.
    * 해당 위치에 바이러스가 없다면 0을 출력한다.
    * 시험관의 가장 왼쪽 위는 (1, 1)부터 시작한다.

입력 조건
- 첫째 줄에 자연수 N, K가 주어지며 각 자연수는 공백으로 구분한다.
    * (1 <= N <= 200, 1 <= K <= 1,000)
- 둘째 줄부터 N개의 줄에 걸쳐서 시험관의 정보가 주어진다.
    * 각 행은 N개의 원소로 구성되며, 해당 위치에서 존재하는 바이러스의 번호가 주어지며 공백으로 구분한다.
    * 단, 해당 위치에 바이러스가 존재하지 않는 경우 0이 주어진다.
    * 모든 바이러스의 번호는 K 이하의 자연수이다.
- N + 2번째 줄에는 S, X, Y가 주어지며 공백으로 구분한다.
    * (0 <= S <= 10,000, 1 <= X, Y <= N)

출력 조건
- S초 뒤에 (X, Y)에 존재하는 바이러스의 종류를 출력한다.
    * 바이러스가 없다면 0을 출력한다.
"""

# 풀이 제한 시간 : 50분
# 2020/11/18 10:30 A.M. ~ 11:03 A.M.
# 실패 - 컴파일 시간 초과

n, k = map(int, input().split())

graph =[]
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def virus(r, c, k):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if nr >= 0 and nr < n and nc >=0 and nc < n:
            if graph[nr][nc] == 0:
                graph[nr][nc] = k

for t in range(1, s+1):

    virus_location = []
    for i in range(n):
        for j in range(n):
            if graph[i][j] != 0:
                virus_location.append((graph[i][j], i, j))

    for vl in sorted(virus_location):
        virus(vl[1], vl[2], vl[0])

print(graph[x-1][y-1])