"""
위상 정렬 알고리즘 소스코드
- 위상 정렬 : 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것
- 진입차수(Indegree) : 특정한 노드로 들어노는 간선의 개수
- 알고리즘 수행 순서
    1. 진입 차수가 0인 노드를 큐에 넣는다.
    2. 큐가 빌 때 까지 다음의 과정을 반복한다.
        (1) 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다.
        (2) 새롭게 진입차수가 0이 된 노드를 큐에 넣는다.
- 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 존재한다고 판단할 수 있다.
    * 여기서는 사이클이 발생하는 것은 고려하지 않는다.
- 알고리즘을 수행하는 동안 큐에서 빠져나간 노드를 순서대로 출력하면 수행 결과를 확인할 수 있다.
- 시간 복잡도 : O(V + E) // E : 노드의 개수, V : 간선의 개수
"""

from collections import deque # 큐를 구현하기 위한 라이브러리

# 노드의 개수와 간선의 개수를 입력받기
v, e = map(int, input().split())
# 모든 노드에 대한 진입차수를 0으로 초기화
indegree = [0] * (v + 1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v + 1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 a에서 b로 방향을 갖는 간선의 존재를 의미
    indegree[b] += 1 # b의 진입차수를 증가

# 위상 정렬 알고리즘 수행
def topology_sort():
    result = [] # 알고리즘 수행 결과를 담을 리스트
    q = deque() # 큐를 구현하기 위한 deque 라이브러리 사용

    # 처음 시작할 때는 진입차수가 0인 노르를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    # 큐가 빌 때까지 반복
    while q:
        # 큐에서 원소 꺼내고 result에 담기
        now = q.popleft()
        result.append(now)
        # 해당 원소와 연결된 노드들의 진입차수를 1씩 감소
        for i in graph[now]:
            indegree[i] -= 1
            # 새롭게 진입차수가 0이 되는 노드가 있으면 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    # 위상 정렬을 수행한 결과 출력
    for i in result:
        print(i, end=' ')

topology_sort()