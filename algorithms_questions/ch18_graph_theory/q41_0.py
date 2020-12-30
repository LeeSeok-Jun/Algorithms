"""
여행 계획
- 한울이가 사는 나라에는 N개의 여행지가 1 ~ N번까지의 번호로 구분된다.
- 임의의 두 여행지 사이에는 두 여행지를 연결하는 도로가 존재할 수 있다.
- 도로가 존재할 경우 양방향으로 이동이 가능하다는 의미이다.
- 한울이는 하나의 여행 계획을 세운 뒤에 이 여행 계획이 가능한지의 여부를 판단하려고 한다.
- 여행지의 개수와 여행지 간의 연결 정보가 주어졌을 때, 한울이의 여행계획이 가능한지 여부를 판별하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 여행지의 수 N과 여행 계획에 속한 도시의 수 M이 주어진다.
- 다음 N개의 줄에 걸쳐 N * N 행렬을 통해 임의의 두 여행지가 서로 연결되어 있는지 여부가 주어진다.
    * 값이 1이면 서로 연결되었다는 의미이며, 0이라면 서로 연결되어 있지 않다는 의미이다.
- 마지막 줄에 한울이의 여행 계획에 포함된 여행지의 번호들이 주어지며 공백으로 구분된다.

출력 조건
- 첫째 줄에 한울이의 여행 계획이 가능하다면 YES를, 불가능하다면 NO를 출력한다.
"""

# 풀이 제한 시간 : 40분
# 2020/12/29 10:35 ~ 10:55
# 실패 - 여행 계획에 속한 모든 노드가 같은 집합에 속하면 가능한 여행 경로(서로소)

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())
parent = [0] * (n + 1)

for i in range(1, n+1):
    parent[i] = i

"""
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
"""

# 행렬 입력받기
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        # 연결된 노드들의 경우 union 연산 진행
        if data[j] == 1:
            union_parent(parent, i + 1, j + 1)

plan = list(map(int, input().split()))
result = True

# plan에 속한 노드들이 같은 부모 노드를 공유하고 있다면 가능한 여행 경로
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]):
        result = False

if result:
    print("YES")
else:
    print("NO")