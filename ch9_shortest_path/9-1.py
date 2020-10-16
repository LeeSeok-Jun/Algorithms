"""
간단한 다익스트라 알고리즘 소스코드
- 방향이 존재하고 음의 간선이 없는 그래프에 대해서 수행
- 시간 복잡도 : O(V^2) // V : 노드의 개수
- 전체 노드의 개수가 5,000개 이하라면 일반적으로 사용 가능
- 전체 노드의 개수가 10,000개 이상이면 해결 어려움
"""

import sys
input = sys.stdin.readline # 입력되는 데이터 수가 많음을 대비하여 입력 방법을 sys 라이브러리로 변경
INF = int(1e9) # 무한이 큰 수를 10억으로 설정

# 노드의 개수, 간선의 개수 입력
n, m = map(int, input().split())
# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n + 1)]

# 방문한 적이 있는지 체크하는 목적의 리스트 만들기
visited = [False] * (n + 1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))

# 방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n + 1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        # j[0] = start 노드에서 이어진 노드 번호
        # j[1] = start 노드에서 이어진 노드까지의 거리
        distance[j[0]] = j[1] # 해당 노드번호까지의 최단거리를 j[1]의 값으로 설정

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost # 기존 distance에 저장된 값을 변경

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