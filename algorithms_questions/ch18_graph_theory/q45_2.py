"""
최종 순위 - 3회차
"""

# 풀이 제한 시간 : 60분
# 2021/01/28 13:33 ~ 14:11
# 실패
# 위상정렬 알고리즘에서 하위 노드들은 모두 상위 노드에 연결되어야 한다.
# 위상정렬 알고리즘에서 부모노드 찾기 연산, 결합 연산은 필요 없다.

from collections import deque

import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    
    graph = [[] for _ in range(n+1)]

    data = list(map(int, input().split()))

    # 순위가 높은 노드들은 모두 하위 노드에 연결되어 있어야 한다!
    indegree = [0] * (n+1)
    for i in range(n):
        for j in range(i+1, n):
            graph[data[j]].append(data[i])
            indegree[data[i]] += 1

    m = int(input())

    for i in range(m):
        a, b = map(int, input().split())

        if b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
        
        # elif a in graph[b]:
        else:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1

    cycle = False
    certain = True

    q = deque()
    result = []

    # 먼저 진입차수가 0인 노드들을 큐에 삽입
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    # queue가 빌 때까지가 아닌 노드의 수 만큼 반복
    for _ in range(n):
        # 모든 반복이 끝나기 전에 큐가 빈다면 사이클이 발생한 것
        if len(q) == 0:
            cycle = True
            break

        # 큐에 2개 이상의 노드가 있다는 것은 확실한 순위를 매길 수 없다는 것
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