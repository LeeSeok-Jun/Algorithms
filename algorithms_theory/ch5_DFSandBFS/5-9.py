"""
BFS(너비 우선 탐색 알고리즘)
- BFS의 동작 과정은 다음과 같다.
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리를 한다.
    2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
    3. 2의 과정을 더 이상 수행할 수 없을 때 까지 반복한다.
- 노드의 탐색 순서는 노드가 큐에 들어간 순서이다.
- 데이터의 개수가 N개인 경우 O(N)의 시간 소요
"""

from collections import deque # 큐 자료구조 사용을 위한 모듈 선언

# BFS 메서드 정의
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때 까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 연결된 정보를 리스트 자료형으로 표현(2차원 리스트)
# n 번째 행은 n번 노드가 연결되어 있는 노드의 번호를 의미
graph = [
    [],             # 0번 노드 -> 존재 X
    [2, 3, 8],      # 1번 노드 -> 2번, 3번, 8번과 연결
    [1, 7],         # 이하 생략
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드의 방문 여부를 확인하는 1차원 리스트 정의(각 인덱스는 0 ~ 8번 노드에 상응)
visited = [False] * 9 # default = False, 방문 시 = True

# 정의된 BFS 함수 호출
bfs(graph, 1, visited)