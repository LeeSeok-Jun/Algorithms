"""
전보
- 어느 나라에 N개의 도시가 있다.
- 각 도시는 다른 도시로 전보를 통해 메시지를 전송할 수 있다.
- 전보를 보내기 위해서는 반드시 도시 사이에 통로가 설치되어 있어야 한다.
- 이 통로는 방향성을 가지고 있어서 양방향 설치가 아닌 경우 한 쪽으로만 전송이 가능하다.
- 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
- 만일, 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때,
  C도시에서 최대한 많은 도시로 메시지를 보내면 메시지를 받게 되는 도시의 총 개수와 모두 메시지를 받는 시간을 계산하는 프로그램을 작성하라.

입력 조건
- 첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.(1 <= N <= 30,000, 1 <= M <= 200,000, 1 <= C <= N)
- 둘째 줄부터 M + 1번째 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다.
  이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미다. (1 <= X, Y <= N, 1 <= Z <= 1,000)

출력 조건
- 첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
"""

import heapq # 우선순위 큐를 이용하여 다익스트라 알고리즘 구현
import sys # 한 번에 많은 양의 데이터를 입력받기위해 사용

input = sys.stdin.readline
INF = int(1e9) # 임의의 무한을 의미하는 값

# 노드의 개수, 간선의 개수, 시작 노드를 입력
n, m, start = map(int, input().split())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보 입력
for _ in range(m):
    x, y, z = map(int, input().split())
    # X번 노드에서 Y번 노드로 가는 비용이 Z
    graph[x].append((y, z))

# 우선순위 큐를 이용한 다익스트라 알고리즘 구현
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로를 0으로 설정하여 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    # 우선순위 큐가 모두 빌 때까지
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보(거리와 노드 번호)를 꺼냄
        dist, now = heapq.heappop(q)
        # 이미 최단거리를 기록하였으면 생략
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            # i[0] = now 노드와 연결돤 노드 번호
            # i[1] = now 노드와 연결된 노드까지 간선의 비용
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            # 거리를 갱신하고 새롭게 큐에 삽입
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 도달할 수 있는 노드의 개수
count = 0
# 도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
max_distance = 0
for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

# 시작 노드는 제외해야 하므로 count - 1을 출력
print(count - 1, max_distance)