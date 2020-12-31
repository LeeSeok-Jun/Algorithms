"""
여행 계획 - 2회차
"""

# 풀이 제한 시간 : 40분
# 2020/12/31 10:06 ~ 10:23
# 같은 부모 노드를 갖는 지 판단하는 방법이 틀림

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

parent = [0] * n
for i in range(n):
    parent[i] = i

for i in range(n):
    data = list(map(int, input().split()))

    for j in data:
        if data[j] == 1:
            union_parent(parent, i, j) 

plan = list(map(int, input().split()))

result = True

"""
for i in range(len(plan)):
    for j in range(i+1, len(plan)):
        if find_parent(parent, i) != find_parent(parent, j):
            result = False
"""

for i in range(m-1):
    if find_parent(parent, plan[i]-1) != find_parent(parent, plan[i+1]-1):
        result = False

if result:
    print("YES")
else:
    print("NO")