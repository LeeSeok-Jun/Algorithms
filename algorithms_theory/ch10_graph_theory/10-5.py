"""
크루스칼 알고리즘 소스코드
- 최소 비용 신장 트리를 만드는 알고리즘
    * 신장 트리 : 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프
- 그리디 알고리즘으로 분류
- 알고리즘 수행 순서
    1. 간선 데이터를 비용에 따라 오름차순으로 정렬한다.
    2. 간선을 하나씩 확인하여 현재의 간선이 사이클을 발생시키는지 확인한다.
        (1) 사이클이 발생하지 않는 경우 최소 신장 트리에 포함시킨다.
        (2) 사이클이 발생하는 경우 최소 신장 트리에 포함시키지 않는다.
    3. 모든 간선에 대하셔 2번의 과정을 반복한다.
- 신장 트리에 포함되는 간선의 개수는 '노드의 개수 - 1'
- 간선의 개수가 E일때 시간 복잡도 : O(ElogE)
"""

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 노드의 개수와 간선(union 연산)의 수 입력받기
# v : 노드 // e : 간선
v, e = map(int, input().split())
parent = [0] * (v + 1) # 부모 노드를 저장하는 테이블 초기화

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges= []
result = 0

# 부모 테이블상에서 먼저 부모 노드를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

# 모든 간선에 대한 정보를 입력 받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((cost, a, b))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 비용이 낮은 것 부터 하나씩 확인
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)