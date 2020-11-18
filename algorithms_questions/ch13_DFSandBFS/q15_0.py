"""
특정 도시의 거리 찾기
- https://www.acmicpc.net/problem/18352
- 어떤 나라에 1 ~ N번까지의 도시와 모두 거리가 1인 M개의 단방향 도로가 존재한다.
- 특정한 도시 X로 부터 출발하여 도달할 수 있는 모든 도시 중에서, 최단 거리가 정확히 K인 모든 도시의 번호를 출력하는 프로그램을 작성하시오.
- 또한 출발 도시 X에서 출발 도시 X로 가는 최단 거리는 항상 0이라고 가정한다.

입력 조건
- 첫째 줄에 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X가 주어진다.
    * (2 <= N <= 300,000, 1 <= M <= 1,000,000, 1 <= K <= 300,000, 1 <= X <= N)
- 둘째 줄부터 M개의 줄에 걸쳐서 두 개의 자연수 A, B가 주어지며, 각 자연수는 공백으로 구분한다.
    * 이는 A번 도시에서 B번 도시로 이동하는 단방향 도로가 존재한다는 의미이다. (1 <= A, B <= N)
    * 단, A와 B는 서로 다른 자연수이다.

출력 조건
- X로부터 출발하여 도달할 수 있는 도시 중에서, 최단 거리가 K인 모든 도시의 번호를 한 줄에 하나씩 오름차순으로 출력한다.
- 이때 도달할 수 있는 도시 중에서, 최단 거리가 K인 도시가 하나도 존재하지 않으면 -1을 출력한다.
"""

# 풀이 제한 시간 : 30분
# 2020/11/17 01:25 P.M. ~
# 실패 - 문제 접근 방식이 잘못 되었다.
# 그래프에서 모든 간선의 비용이 동일할 때는 BFS(너비 우선 탐색)을 이용하여 최단 거리를 찾을 수 있다.

from collections import deque # 큐 구현을 위한 패키지 호출

n, m, k, x = map(int, input().split())

roads = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    roads[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시에서 출발 도시까지는 0

# BFS 수행
q = deque([x]) # 큐에 출발 도시 삽입
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next in roads[now]:
        # 아직 방문하지 않은 도시의 경우
        if distance[next] == -1:
            # 현재 도시에서 다른 도시까지의 거리는 모두 1이므로 다음 도시의 거리는 현재 도시까지의 거리에서 1이 늘어남
            distance[next] = distance[now] + 1 
            q.append(next)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
