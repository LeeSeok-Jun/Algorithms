"""
어두운 길 - 2회차
"""

# 풀이 제한 시간 : 40분
# 2020/12/31 10:43 ~ 10:51
# 정답

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(paretn, a, b):
    a = find_parent(parent, a)
    b = find_parent(paretn, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * n
for i in range(n):
    parent[i] = i

edges = []
for _ in range(m):
    x, y, z = map(int, input().split())

    edges.append((z, x, y))

edges.sort()

result = 0
for edge in edges:
    z, x, y = edge

    result += z
    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result -= z

print(result)