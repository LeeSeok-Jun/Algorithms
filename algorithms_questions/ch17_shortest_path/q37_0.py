"""
플로이드
- https://www.acmicpc.net/problem/11404
- N(1 <= N <= 100)개의 도시가 있고, 한 도시에서 출발하여 다른 도시에 도착하는 M(1 <= M <= 100,000)개의 버스가 있다.
- 각 버스는 한 번 사용할 때 필요한 비용이 있다.
- 모든 도시의 쌍 (A, B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 도시의 개수 N이 주어진다.
- 둘째 줄에 버스의 개수 M이 주어진다.
- 셋째 줄 부터 M+2 줄까지 다음과 같은 버스의 정보가 주어진다.
    * 먼저 해당 버스의 출발 도시의 번호가 주어진다.
    * 버스의 정보는 버스의 시작 도시 A, 도착 도시 B, 한 번 타는데 필요한 비용 C로 이루어져 있다.
    * 시작 도시와 도착 도시가 같은 경우는 없다.
    * 비용은 100,000보다 작거나 같은 자연수이다.
- 시작 도시와 도착 도시를 연결하는 노선은 하나가 아닐 수 있다.

출력 조건
- N개의 줄을 출력한다.
- i번째 줄에 j번째 숫자는 도시 i에서 j로 가는데 필요한 최소 비용이다.
- 갈 수 없는 경우 그 자리에 0을 출력한다.
"""

# 풀이 제한 시간 : 40분
# 2020/12/22 09:45 ~ 10:00`
# 실패 - 컴파일 시간 초과
# a,b,c 입력 시 min 보다는 직접 비교로 시간 줄이기
# graph의 원소 중 최종 값이 INF인 경우 0으로 출력하는 경우 빼먹음

n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for r in range(n):
    for c in range(n):
        if r == c:
            graph[r][c] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < graph[a-1][b-1]:
        graph[a-1][b-1] = c

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(n):
    for j in range(n):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()