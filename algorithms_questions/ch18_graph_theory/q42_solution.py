"""
탑승구 - 문제 해설
"""

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
p = int(input())

data = []
for _ in range(p):
    data.append(int(input()))

parent = [0] * (g + 1)
for i in range(1, g+1):
    parent[i] = i

result = 0
for d in data:
    # 비행기가 도킹 가능한 게이트의 번호가 가장 큰 값을 확인
    plane = find_parent(parent, d)
    # 해당 게이트의 부모 노드가 0인 경우 더 이상 도킹 불가능
    if plane == 0:
        break
    
    # 도킹이 가능한 경우 번호가 하나 작은 게이트와 집합을 합침
    union_parent(parent, plane, plane-1)
    result += 1

print(result)