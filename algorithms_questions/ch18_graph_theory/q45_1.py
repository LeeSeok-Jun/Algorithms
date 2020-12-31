"""
최종 순위 - 2회차
"""

# 풀이 제한 시간 : 60분
# 2020/12/31 11:10 ~ 11:31
# 실패 - 자료의 사용(data[i])에 실수, 큐에 처음 초기화를 안함

from collections import deque

"""
# 위상 정렬 알고리즘에서는 사용할 필요가 없다.

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
"""

for tc in range(int(input())):

    n = int(input())

    parent = [0] * (n + 1)
    for i in range(1, n+1):
        parent[i] = i

    indegree = [0] * (n+1)

    data = list(map(int, input().split()))

    graph = [[] for _ in range(n+1)]

    # data[i]와 data[j]를 사용해야함!
    for i in range(n):
        for j in range(i+1, n):
            graph[data[j]].append(data[i])
            indegree[data[i]] += 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())

        if b not in graph[a]:
            graph[b].remove(a)
            indegree[a] -= 1

            graph[a].append(b)
            indegree[b] += 1

        else:
            graph[a].remove(b)
            indegree[b] -= 1

            graph[b].append(a)
            indegree[a] += 1

    cycle = False
    certain = True


    q = deque()
    result = []

    # 맨 처음 queue에 원소를 집어 넣는 것을 뺌
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    for _ in range(n):
        if len(q) == 0:
            cycle = True
            break

        if len(q) >= 2:
            certain = False
            break

        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in reversed(result):
            print(i, end=" ")
        print()
