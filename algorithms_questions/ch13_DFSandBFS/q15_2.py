"""
특정 거리의 도시 찾기 - 3회차
"""

# 풀이 제한 시간 : 30분
# 2021/01/18 14:14 ~ 14:35
# 성공 - 그러나 input를 sys 패키지를 통해 해야 시간초과 안나옴

from collections import deque

# 시간을 줄이기 위한 입력 메소드 변경
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())

data = [[] for _ in range(n+1)]
distance = [0] * (n+1)
visited = [False] * (n+1)
visited[x] = True

for _ in range(m):
    a, b = map(int, input().split())
    data[a].append(b)

q = []
q = deque()
q.append(x)

while q:
    now = q.popleft()

    for d in data[now]:
        if not visited[d]:
            q.append(d)
            visited[d] = True
            distance[d] = distance[now] + 1

temp = False
for i in range(1, n+1):
    if distance[i] == k:
        temp = True
        print(i)

if temp == False:
    print(-1)
        

