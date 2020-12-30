"""
최종 순위
- https://www.acmicpc.net/problem/3665
"""

# 풀이 제한 시간 : 60분
# 2020/12/30 11:30 ~
# 실패 - 문제가 어려움...

from collections import deque

for tc in range(int(input())):
    n = int(input())

    graph = [[] for _ in range(n+1)] # 간선 정보 테이블
    indegree = [0] * (n + 1) # 진입 차수 테이블

    data = list(map(int, input().split()))
    # 간선 정보와 진입 차수 저장
    for i in range(n):
        for j in range(i+1, n):
            graph[data[j]].append(data[i])
            indegree[data[i]] += 1

    m = int(input())

    for _ in range(m):
        a, b = map(int, input().split())

        # 간선 방향 뒤집고 진입 차수 고치기
        if b in graph[a]:
            graph[a].remove(b)
            indegree[b] -= 1
            graph[b].append(a)
            indegree[a] += 1
        else:
            graph[b].remove(a)
            indegree[a] -= 1
            graph[a].append(b)
            indegree[b] += 1



    # 위상 정렬 알고리즘
    
    # 노드의 수 만큼 위상정렬 알고리즘을 수행
    # 그 전에 큐가 빌 경우, 사이클이 발생한 것으로 간주하여 위상 정렬 불가능
    # 큐에 한 번에 2개 이상의 원소가 들어올 경우, 가능한 정렬 결과가 여러개
    # 큐에 원소가 항상 1개만 들어올 경우, 고유한 순위가 존재
    
    result = []
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    certain = True
    cycle = False

    for i in range(n):
        # 반복이 끝나기 전 큐가 비어있다면, 사이클 발생
        if len(q) == 0:
            cycle = True
            break

        # 큐의 원소가 2개 이상이면, 정렬 결과가 여러개
        if len(q) >= 2:
            certain = False
            break

        # 위상 정렬 알고리즘 진행
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i] -= 1

            if indegree[i] == 0:
                q.append(i)

    # 결과 출력
    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in reversed(result):
            print(i, end=" ")
        print()