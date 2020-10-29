"""
개선된 서로소 집합 알고리즘
- 10-1.py의 find_parent 함수를 10-2.py의 형태로 변경
- 시간 복잡도 O(V + M(1 + log_(2-M/V)_V))
    * 노드의 개수 : V // 최대 union 연산 : V - 1 // find 연산 횟수 : M
"""

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

# union 연산을 각각 수행
for i in range(e):
    a, b = map(int, input().split())
    union_parent(parent, a, b)

# 각 원소가 속한 집합 출력
print('각 원소가 속한 집합 : ', end=' ')
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')

print()

# 부모 테이블 내용 출력
print('부모 테이블 : ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')