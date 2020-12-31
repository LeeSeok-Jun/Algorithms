"""
탑승구 - 2회차
"""

# 풀이 제한 시간 : 50분
# 2020/12/31 10:28 ~ 10:42
# 도킹 가능한 여부 판별 방법 잘못됨

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

g = int(input())

parent = [0] * (g + 1)
for i in range(g+1):
    parent[i] = i

p = int(input())

"""
plane = []
for _ in range(p):
    plane.append(int(input()))

result = 0
for i in range(p):
    if find_parent(parent, plane[i]) != find_parent(parent, plane[i]-1):
        union_parent(parent, plane[i], plane[i]-1)
        result += 1
"""

data = []
for _ in range(p):
    data.append(int(input()))

result = 0
for d in data:
    plane = find_parent(parent, d)

    if plane == 0:
        break

    union_parent(parent, plane, plane-1)
    result += 1

print(result)