"""
정확한 비교
- 선생님은 시험을 본 학생 N명의 성적을 분실하고 성적을 비교한 결과의 일부만 가지고 있다.
- A번 학생의 성적이 B번 학생의 성적보다 낮다면 화살표가 A에서 B를 가리키도록 한다.
- 이 방법으로는 순위를 정확히 알 수도 있는 학생도 있고, 알 수 없는 학생도 존재한다.
- 학생들의 성적을 비교한 결과가 주어질 때, 성적 순위를 정확히 알 수 있는 학생은 모두 몇 명인지 계산하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 학생들의 수 N과 두 학생의 성적을 비교한 횟수 M이 주어진다.
- 다음 M개의 줄에는 두 학생의 성적을 비교한 결과를 나타내는 두 양의 정수 A와 B가 주어진다.
    * A번 학생의 성적이 B번 학생보다 낮다는 것을 의미한다.

출력 조건
- 첫째 줄에 성적 순위를 정확히 알 수 없는 학생이 몇 명인지 출력한다.
"""

# 풀이 제한 시간 : 40분
# 2020/12/22 10:11 ~ 10:35
# 플로이드-위셜 알고리즘으로 최단 경로 구하기
# a와 b에 대해서 a에서 b의 경로가 있거나 반대로 b에서 a로 경로가 있다면 성적 비교 가능
# 성적 비교 가능 횟수가 전체 학생의 수 만큼 가능하다면 정확한 성적을 알 수 있다.

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * n for _ in range(n)]

for r in range(n):
    for c in range(m):
        if r == c:
            graph[r][c] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a-1][b-1] = 1

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = 0
for i in range(n):
    count = 0

    for j in range(n):
        # 두 학생(i번, j번) 간의 성적 비교가 가능한지 확인
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1

    # 성적 비교 횟수가 학생 수와 같다면 i번 학생은 정확한 등수를 알 수 있다.
    if count == n:
        result += 1

print(result)