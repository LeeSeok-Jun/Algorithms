"""
플로이드 워셜 알고리즘 소스코드
- 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구해야 하는 경우 사용
- 다이나믹 프로그래밍의 특성을 갖는다.
- 시간 복잡도 : O(N^3) // N : 노드의 수
- 특정 k단계에 대한 점화식은 다음과 같다.
    D[ab] = min(D[ab], D[ak] + D[kb])
"""
# 2020/10/22

INF = int(1e9) # 무한의 의미하는 값으로 10억 설정

# 노드의 개수 및 간선의 개수 입력
n = int(input())
m = int(input())

# 2차원 리스트로 그래프를 표현하고 모든 값을 무한으로 초기화
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력하여 그래프를 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따른 플로이드 워셜 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        # 도달할 수 없는 경우 "INFINITY" 출력
        if graph[a][b] == INF:
            print("INFINITY", end=" ")
        # 도달할 수 있는 경우 거리 출력
        else:
            print(graph[a][b], end=" ")
    print()