"""
화성 탐사
- 화성 탐사 로봇이 에너지를 효율적으로 사용하고자 출발 지점부터 목표 지점까지 이동할 때, 항상 최적의 경로를 찾도록 개발해야한다.
- 로봇이 존재하는 공간은 N * N 크기의 2차원 공간이며, 각각의 칸을 지나기 위한 비용이 존재한다.
- 가장 위쪽칸인 (0, 0)부터 가장 오른쪽 아래 칸인 (N-1, N-1) 위치로 이동하는 최소비용을 출력하는 프로그램을 작성하시오.
- 로봇은 특정한 위치에서 상하좌우로 인접한 곳으로 1칸씩 이동할 수 있다.

입력 조건
- 첫째 줄에 테스트 케이스의 수 T가 주어진다.
- 매 테스트 케이스의 첫째 줄에는 탐사 공간의 크기를 의미하는 정수 N이 주어진다.
- 이어서 N개의 줄에 걸쳐 가 칸의 비용이 주어지며 공백으로 구분한다.

출력 조건
- 각 테스트 케이스마다 문제에서 제시한 최소비용을 한 줄에 하나씩 출력한다.
"""

# 풀이 제한 시간 : 40분
# 2020/12/23 09:32 ~ 10:12
# 실패 - 시간초과
# 로직은 맞다. (../algorithms_theory/ch9_shortest_path/9-2.py 참고)

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for tc in range(int(input())):

    n = int(input())

    distance = [INF] * (n * n)

    data = []
    for i in range(n):
        data.append(list(map(int, input().split())))

    graph = [[] for _ in range(n*n)]
    for r in range(n):
        for c in range(n):
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]

                if nr >= 0 and nr < n and nc >= 0 and nc < n:
                    graph[r*n+c].append((nr*n+nc, data[nr][nc]))

    q = []
    heapq.heappush(q, (data[0][0], 0))
    distance[0] = data[0][0]

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    print(distance[len(distance) - 1])

