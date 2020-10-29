"""
경로 압축 기법
- 10-1.py에서 구현한 서로소 집합 알고리즘에서 find 함수를 실행 시 최악의 경우 시간 복잡도 O(V)
    * union 연산의 수가 M일 때, 최악의 시간 복잡도 O(VM)
- 이 문제는 부모 노드를 저장하고 있는 테이블에서 상위 노드의 최상단 노드를 부모 노드로 설정하므로 해결
"""

# 10-1.py의 find_parent 함수를 다음과 같이 변경하면 해결 가능

# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] =  find_parent(parent, parent[x])
    return parent[x]