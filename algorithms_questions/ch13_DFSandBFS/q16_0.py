"""
연구소
- https://www.acmicpc.net/problem/14502
- 인체에 치명적인 바이러스가 연구소에서 유출되었고 바이러스의 확산을 막기 위해서 연구소에 벽을 세우려고 한다.
- 연구소는 크기가 N * M인 직사각형으로 나타낼 수 있으며, 직사각형은 1 * 1 크기의 직사각형으로 나뉘어 있다.
- 연구소는 빈 칸, 벽으로 이루어져 있그며 벽은 칸 하나를 가득 차지한다.
- 일부 칸은 바이러스가 존재하며, 이 바이러스는 상하좌우로 인접한 빈칸으로 모두 퍼져나갈 수 있다.
- 새로 세울 수 있는 벽의 개수는 3개이며 꼭 3개를 모두 세워야 한다.
- 연구소의 지도가 주어졌을 때 얻을 수 있는 안전 영역 크기의 최댓값을 구하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 지도의 세로 크기 N과 가로 크기 M이 주어진다. (3 <= N, M <= 8)
- 둘째 줄 부터 N개의 줄에 지도의 모양이 주어진다.
    * 0은 빈 칸, 1은 벽, 2는 바이러스가 있는 위치
    * 2의 개수는 2보다 크거나 같고 10보다 작거나 같은 자연수이다.
- 빈 칸의 개수는 3개 이상

출력 조건
- 첫째 줄에 얻을 수 있는 안전 영역의 최대 크기를 출력한다.
"""

# 풀이 제한 시간 : 40분
# 2020/11/17 01:55 P.M. ~
# 실패

from itertools import combinations # 조합을 사용하기 위해 외장 함수 호출

n, m = map(int, input().split())

graph = []
vacancy = [] # 0
wall = [] # 1
virus = [] # 2 

for r in range(n):
    data = list(map(int, input().split()))
    graph.append(data)
    for c in range(len(data)):
        if graph[r][c] == 0:
            vacancy.append((r, c))
        elif graph[r][c] == 1:
            wall.append((r, c))
        elif graph[r][c] == 2:
            virus.append((r, c))

candidates = list(combinations(vacancy, 3))

answer = -1
for candidate in candidates:
    for new_wall in candidate:
        graph[new_wall[r]][new_wall[c]] = 1

    for v in virus:
        pass

def dfs(r, c):
    if r <= -1 or r >= n or c <= -1 or c >= m:
        return False
    if graph[r][c] == 0:
        graph[r][c] = 2
        dfs(r - 1, c) # 상
        dfs(r, c - 1) # 좌
        dfs(r + 1, c) # 하
        dfs(r, c + 1) # 우
        return True
    return True