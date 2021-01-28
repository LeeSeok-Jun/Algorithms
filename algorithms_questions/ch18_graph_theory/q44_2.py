"""
행성 터널 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/27 15:12 ~
# 실패 - 틀린 부분 주석 처리

import sys
input = sys.stdin.readline

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

# 내가 생각한 방법
"""
planet = []
for _ in range(n):
    x, y, z = map(int, input().split())
    planet.append((x, y, z))

x_edges = []
y_edges = []
z_edges = []

for i in range(len(planet) - 1):
    x_edges.append((abs(planet[i][0] - planet[i+1][0]), i, i+1))
    y_edges.append((abs(planet[i][1] - planet[i+1][1]), i, i+1))
    z_edges.append((abs(planet[i][2] - planet[i+1][2]), i, i+1))

x_edges.sort()
y_edges.sort()
z_edges.sort()
"""

# 문제 풀이
x = []
y = []
z = []

for i in range(n):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

edges = []
for i in range(n-1):
    edges.append((x[i+1][0] - x[i][0], x[i][1], x[i+1][1]))
    edges.append((y[i+1][0] - y[i][0], y[i][1], y[i+1][1]))
    edges.append((z[i+1][0] - z[i][0], z[i][1], z[i+1][1]))

edges.sort()

# 크루스칼 알고리즘
answer = 0

for edge in edges:
    cost, a, b = edge

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(answer)