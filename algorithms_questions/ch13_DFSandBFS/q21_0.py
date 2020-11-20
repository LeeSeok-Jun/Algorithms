"""
인구 이동
- https://www.acmicpc.net/problem/16234
- 1 * 1 의 칸으로 나누어진 N * N 크기의 땅이 존재한다.
- 각각의 땅에는 나라가 하나씩 존재하며, r행 c열에는 A[r][c]명이 살고 있다.
- 인접한 나라에는 국경선이 존재하며 모든 나라는 1 * 1 크기이기 때문에 정사각형 형태를 띄고있다.
- 인구 이동이 시작되는데 인구이동은 다음과 같이 진행되고, 더 이상 아래 방법에 의해 인구 이동이 없을 때 까지 반복
    * 국경선을 공유하는 두 나라의 인구 차이가 L명 이상 R명 이하이면 국경선 개방
    * 조건에 맞는 모든 나라의 국경선이 열렸다면 인구이동 시작
    * 인구이동은 인접한 칸 만을 이동할 수 있으며, 그 나라를 연합이라고 한다.
    * 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. (소수점 버림)
    * 연합을 해체하고 모든 국경선을 닫는다.
- 각 나라의 인구수가 주어졌을 때, 인구 이동이 몇 번 발생하는지 구하는 프로그램을 작성하시오.

입력 조건
- 첫째 줄에 N, L, R이 주어진다.
    * (1 <= N <= 50, 1 <= L <= R <= 100)
- 둘째 줄부터 N개의 줄에 각 나라의 인구수가 주어진다.
    * r행 c열에 주어지는 정수는 A[r][c]의 값이다.
    * (0 <= A[r][c] <= 100)

출력 조건
- 인구 이동이 몇 번 발생하는지 첫째 줄에 출력한다.
"""

# 풀이 제한 시간 : 40분
# 2020/11/20 11:20 A.M. ~ 12:11 P.M.
# BFS를 이용한 문제 접근은 맞았으나 설계가 잘못됨

from collections import deque # 큐 자료구조 사용을 위한 모듈 선언

n, least, large = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

answer = 0

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

for r in range(n):
    for c in range(n):
        queue = deque([(r, c)])
        count = 1
        total = A[r][c]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                if abs(A[r][c] - A[nr][nc]) >= least and abs(A[r][c] - A[nr][nc]) <= large:
                    queue.append((nr, nc))
                    count += 1
                    total += A[nr][nc]

        moving = int(total / count)
        if count >= 2:
            answer += 1

        print(queue)
        while queue:
            nr, nc = queue.popleft()
            A[nr][nc] = moving

print(answer)