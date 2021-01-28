"""
어두운 길 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/27 14:59 ~ 15:11
# 정답

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

edges = [] * m

answer = 0
for _ in range(m): 
    x, y, z = map(int, input().split())
    edges.append((z, x, y))
    answer += z

edges.sort()

parent = [0] * n
for i in range(n):
    parent[i] = i

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer -= cost

print(answer)
