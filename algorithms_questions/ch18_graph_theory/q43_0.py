"""
어두운 길
- 한 마을은 N개의 집과 M개의 도로로 구성되어 있다.
- 각 집은 0번부터 N-1번까지의 번호로 구분된다.
- 모든 도로에는 가로등이 설치되어 있는데 특정한 도로의 가로등을 하루 동안 켜기 위한 비용은 해당 도로의 길이와 동일하다.
- 정부는 일부 가로등을 비활성화하되, 마을에 있는 임의의 두 집에 대하여 가로등이 켜진 도로만으로도 오갈 수 있도록 만들고자 한다.
- 결과적으로 일부 가로등을 비활성화 하여 최대한 많은 금액을 절약하고자 한다.
- 마을의 집과 도로 정보가 주어졌을 때, 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 집의 수 N과 도로의 수 M이 주어진다.
- 다음 M개의 줄에 걸쳐서 각 도로에 대한 정보 X, Y, Z가 주어지며 공백으로 구분한다.
    * X와 Y사이에 도로가 있으며 그 길이가 Z라는 의미

출력 조건
- 첫째 줄에 일부 가로등을 비활성화하여 절약할 수 있는 최대 금액을 출력한다.
"""

# 풀이 제한 시간 : 40분
# 2020/12/30 10:42 ~ 10:53
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
    result += edge[0]


for edge in edges:
    z, x, y = edge

    if find_parent(parent, x) != find_parent(parent, y):
        union_parent(parent, x, y)
        result -= z

print(result)
        