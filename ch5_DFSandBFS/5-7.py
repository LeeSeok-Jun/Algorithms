"""
그래프를 인접 리스트 방식으로 표현
- 연결된 정보만을 저장하므로 메모리 관리에 효율적
- 연결 정보를 확인하는데 비교적 시간이 걸림
"""

# 행(ROW)이 3개인 2차원리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)