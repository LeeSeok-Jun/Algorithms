"""
인구 이동 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/20 12:45 ~ 13:40
# 틀림 - 나는 dfs로 생각했지만 bfs로 풀어야 함
# 큐를 이용하여 문제 해결, 각 나라의 연합 번호를 설정할 필요가 있다.
# 틀린 부분, 빼먹은 부분 주석 처리

# 큐 자료구조 사용
from collections import deque
import sys
input = sys.stdin.readline

n, min_value, max_value = map(int, input().split())

A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

answer = 0

# index : 연합 번호
def makeUnion(r, c, index):
    current_union = [] # 현재 연합 정보
    current_union.append((r, c))

    queue = deque() # 인접 국가를 BFS로 탐색하기 위한 큐 자료구조 선언
    queue.append((r, c))

    union[r][c] = index
    sum_value = A[r][c]
    count = 1 # 현재 연합의 국가 수

    # BFS
    while queue:
        now_r, now_c = queue.popleft()

        for i in range(4):
            nr = now_r + dr[i]
            nc = now_c + dc[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < n and union[nr][nc] == -1:
                if abs(A[now_r][now_c] - A[nr][nc]) <= max_value and abs(A[now_r][now_c] - A[nr][nc]) >= min_value:
                    # if A[nr][nc] not in current_union:
                    #     current_union.append(A[nr][nc])
                    #     makeUnion(nr, nc)
                    queue.append((nr, nc))

                    union[nr][nc] = index
                    sum_value += A[nr][nc]
                    count += 1
                    current_union.append((nr, nc))

    # 인구 배분
    for i, j in current_union:
        A[i][j] = sum_value // count

    return count    

while True:
    union = [[-1] * n for _ in range(n)] # 연합이 없으면 -1
    index = 0 # 연합 번호

    for i in range(n):
        for j in range(n):
            if union[i][j] == -1:
                makeUnion(i, j, index)
                index += 1

    # 연합의 수가 전체 국가의 수와 같으면 더 이상 연합을 생성할 수 없는 상황
    if index == n * n:
        break

    answer += 1


print(answer)