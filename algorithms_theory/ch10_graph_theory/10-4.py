"""
서로소 집합을 활용한 사이클 판별 소스코드
- 간선에 방향성이 없는 무방향 그래프에서만 적용 가능
    * 방향이 있는 그래프에서는 DFS를 이용하여 확인 가능
"""
# 2020/10/27

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
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

# 부모 테이블상에서 먼저 부모 노드를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i

cycle = False # 사이클 발생 여부를 판별하는 변수

for i in range(e):
    a, b = map(int, input().split())
    # 사이클이 발생한 경우 종료
    # 트리 자료구조에서 간선으로 이어진 두 노드가 같은 루트 노드를 가지고 있다는 것은 사이클이 발생함을 의미한다.
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    # 사이클이 발생하지 않았다면 union(합집합) 수행
    else:
        union_parent(parent, a, b)

if cycle:
    print("사이클이 발생하였습니다.")
else:
    print("사이클이 발생하지 않았습니다.")