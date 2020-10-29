"""
개선된 다익스트라 알고리즘
- 최악의 경우에도 시간 복잡도 O(ElogV) // V : 노드의 수, E : 간선의 수
- 노드 정보를 힙(Heap)에 저장하여 선형 탐색 시간을 로그 탐색 시간으로 간추렸다.
- 힙은 우선순위 큐(Priority Queue)를 이용하여 구현
"""

import heapq # 우선순위 큐 사용(최소힙, 가치가 낮은 순서대로 먼저 삭제)을 위한 라이브러리 패키지 호출
import sys # 빠른 여러줄 입력을 위한 라이브러리 패키지 호출

input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억 설정

# 노드의 개수, 간선의 개수를 입력
n, m = map(int, input().split())

# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 생성
graph = [[] for i in range(n + 1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 개선된 다익스트라 알고리즘
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 우선순위 큐에 삽입
    # 리스트 q를 사용하여 (거리, 노드번호) 형식의 튜플을 사용
    heapq.heappush(q, (0, start))
    distance[start] = 0 # 시작 노드의 최단 거리를 0으로 설정

    # 큐의 내용물이 없을때 까지 반복
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q) # dist = 거리 / now = 해당 노드
        # 현재 노드가 이미 처리된 적이 있으면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            # i[0] : now 노드에서 연결된 노드 번호
            # i[1] : now 노드에서 연결된 노드까지의 거리
            cost = dist + i[1]
            
            # 현재 노드를 거쳐서, 다른 노드를 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, INFINITY라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리 출력
    else:
        print(distance[i])