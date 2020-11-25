"""
특정 거리의 도시 찾기 - 2회차
"""

# 문제 풀이 시간 : 30분
# 2020/11/25 12:20 P.M. ~ 12:30 P.M.


from collections import deque

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
distance[x] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

q = deque()
q.append((x, distance[x]))

while q:
    now, dist = q.popleft()

    for next_city in graph[now]:
        if distance[next_city] == -1:
            distance[next_city] = dist + 1
            q.append((next_city, distance[next_city]))

        # else:
        #     distance[next_city] = min(dist + 1, distance[next_city])
        #     q.append((next_city, distance[next_city]))

exist = False
for i in range(1, n+1):
    if distance[i] == k:
        exist = True
        print(i)

if exist == False:
    print(-1)
    