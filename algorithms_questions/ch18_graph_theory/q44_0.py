"""
행성 터널
- https://www.acmicpc.net/problem/2887
"""

# 풀이 제한 시간 : 40분
# 2020/12/30 10:57 ~ 11:11
# 실패 - 메모리 초과
# 크루스칼 알고리즘의 사용은 맞았으나 간선 비용 계산 측면에서 틀림

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

n = int(input())

parent = [0] * n
for i in range(n):
    parent[i] = i

planets = []
for _ in range(n):
    x, y, z = map(int, input().split())
    planets.append((x, y, z))

edges = []
for i in range(n-1):
    for j in range(i+1, n):
        x1, y1, z1 = planets[i]
        x2, y2, z2 = planets[j]
        cost = min(abs(x1-x2), abs(y1-y2), abs(z1-z2))

        edges.append((cost, i, j))

edges.sort()

result = 0
for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


