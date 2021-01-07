"""
다익스트라 알고리즘(힙)
- 방향이 존재하고 음의 간선이 없는 그래프에 대해서 수행
- 그리디 알고리즘의 특성을 갖음
- 시간 복잡도 O(ElogV)
    * E : 간선의 수
    * V : 노드의 수
"""

import heapq # 우선순위 큐 사용(최소힙)
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())

start = int(input())

# 노드와 간선 정보
graph = [[] for i in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c)) # 노드 A에서 B로 가는 간선이 존재하며 그 비용은 C

# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)

# 다익트스라 알고리즘
def dijkstra(start):
    q = [] # 우선순위 큐에 이용할 리스트 생성

    # 시작 노드를 우선순위 큐에 삽입
    heapq.heappush(q, (0, start)) # (거리, 노드번호)
    distance[start] = 0 # 시작노드에서 시작노드까지 거리는 0

    # 큐가 빌때 까지 반복 수행
    while q:
        # 우선순위 큐에서 가장 거리가 짧은 노드 정보 꺼내기
        dist, now = heapq.heappop(q)

        # 최단 거리 테이블에 저장된 값이 더 작은 경우 해당 노드는 무시
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            # i[0] : 인접 노드의 번호
            # i[1] : 인접 노드까지의 비용
            cost = dist + i[1] # 다음 인접 노드까지의 총 거리

            # 최단 거리 테이블과 비교하여 최단 거리를 새로 갱신함
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) # 갱신할 경우 새로 heap에 추가

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, INFINITY라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])