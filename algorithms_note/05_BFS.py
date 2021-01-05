"""
BFS(너비 우선 탐색 알고리즘)
- 그래프 전체를 탐색하는 방법 중 하나로 탐색 시작 노드와 인접한 노드를 먼저 탐색하는 방법
- '큐' 자료구조를 이용하며 큐에 들어간 노드의 순서가 곧 탐색 순서
    * DFS는 '스택' 자료구조를 이용
- 데이터의 개수가 N인 경우 총 O(N)의 시간 소요
- 알고리즘 진행 과정
    1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
    2. 큐에서 노들르 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
    3. 2의 과정을 더 이상 수행할 수 없을 때 까지 반복
- 일반적으로 반복문을 통해 구현
    * DFS는 재귀적인 방법을 통해 구현
- 최소 거리를 구할 때 BFS를 사용하여 구현할 수 있다.
    * 큐에 노드를 추가하는 경우 상응하는 테이블에 거리 정보를 저장
"""

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    # 큐기 빌 때 까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')

        # 인접 노드 검사
        for i in graph[v]:
            # 방문하지 않은 인접 노드들을 큐에 추가
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 그래프를 인접 리스트 방식으로 표현
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

visited = [False] * 9 # default = False, 방문 시 = True

bfs(graph, 1, visited)