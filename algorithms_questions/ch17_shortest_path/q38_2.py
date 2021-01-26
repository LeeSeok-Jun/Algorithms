"""
정확한 순위 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/26 15:37 ~ 15:58
# 정답! - 조금 수정할 필요는 있음..

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * n for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if i == j:
#             graph[r][c] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for r in range(n):
        for c in range(n):
            graph[r][c] = min(graph[r][c], graph[r][k] + graph[k][c])

import pprint
pprint.pprint(graph)

answer = 0
for i in range(n):
    count = 0

    for j in range(n):
        # 보다 효율적으로 코드 작성하는 법
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

        # 내가 생각한 방법
        # if graph[i][j] != INF:
        #     count += 1
        # if graph[j][i] != INF:
        #     count += 1

    # 만일 행과 열이 같은 부분을 0으로 처리했다면
    # if count == n: 으로 비교하는것이 맞다.
    if count == n-1:
        answer += 1

print(answer)

