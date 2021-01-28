"""
여행 계획 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/27 14:00 ~ 14:16
# 문제 해결 방법은 정답이지만 코드를 좀 더 효율적으로 구성하는 방법을 고민해보자


def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n + 1)
for i in range(1, n):
    parent[i] = i

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

    for j in range(n):
        if graph[i][j] == 1:
            union_parent(parent, i+1, j+1)

plan = list(map(int, input().split()))

# 데이터 입력 과정에서 union_parent 연산을 수행하는것이 더 낫다.(33 ~ 35번줄)
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             union_parent(parent, i+1, j+1)

answer = "YES"
"""
for i in range(len(plan)):
    for j in range(i+1, len(plan)):
        if find_parent(parent, plan[i]) != find_parent(parent, plan[j]):
            answer = "NO"
"""

for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        answer = "NO"

print(answer)