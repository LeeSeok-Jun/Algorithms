"""
서로소 집합 알고리즘
- 서로소 집합 : 공통 원소가 없는 두 집합
- 서로호 집합 자료구조 : 서로소 부분 집합들로 나누어진 원소들의 데이터를 처리하기 위한 자료구조
- union(합집합)과 find(찾기) 2개의 연산으로 조작
- 트리 자료구조를 이용하여 집합 표현
    * 일반적으로 번호가 큰 노드가 번호가 작은 노드를 간선으로 가리키도록 표현
- 서로조 집합 계산 알고리즘
    1 : union(합집합) 연산을 확인하여, 서로 연결된 두 노드 A, B를 확인한다.
        (1) A와 B의 루트 노드 A' 와 B'를 각각 찾는다.
        (2) A'를 B'의 부모 노드로 설정한다. (B'가 A'를 가리키도록 한다.)
    2. 모든 union(합집합) 연산을 처리할 때까지 1번 과정을 반복
- 시간 복잡도 O(V + M(1 + log_(2-M/V)_V))
    * 노드의 개수 : V // 최대 union 연산 : V - 1 // find 연산 횟수 : M
"""

v = int(input()) # 노드의 개수

parent = [0] * (v + 1) # 특정 노드의 부모 노드에 대한 정보를 담는 테이블
# 부모 노드 테이블은 맨 처음 모든 노드들이 자기 자신을 부모 노드로 설정하도록 한다.
for i in range(1, v+1):
    parent[i] = i

# find(찾기) 연산
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# union(합집합) 연산
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 트리 자료구조에서 간선으로 이어진 두 노드가 같은 루트 노드를 가지고 있다는 것은 사이클이 발생함을 의미한다.
def check_cycle(parent, a, b):
    # 사이클 발생
    if find_parent(parent, a) == find_parent(parent, b):
        return True
    # 사이클 없음
    else:
        return False