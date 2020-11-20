from collections import deque # 큐 자료구조 사용을 위한 모듈 선언

n, least, large = map(int, input().split())

A = []
for i in range(n):
    A.append(list(map(int, input().split())))

# 상, 우, 하, 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

answer = 0

# 특정 위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def bfs(x, y, index):
    # 한 연합에 대한 연합 국가들의 정보를 저장하는 리스트
    united = []
    united.append((x, y))
    
    # BFS를 위한 큐 할당
    queue = deque()
    queue.append((x, y))

    union[x][y] = index # 해당 위치 연합 번호 할당
    summary = A[x][y] # 현재 연합의 전체 인구수
    count = 1 # 연합 내 국가의 수

    # BFS
    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dr[i]
            ny = y + dc[i]

            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1:
                if least <= abs(A[x][y] - A[nx][ny]) <= large:
                    queue.append((nx, ny))

                    union[nx][ny] = index # 연합 번호 지정
                    summary += A[nx][ny]
                    count += 1
                    united.append((nx, ny)) # 연합에 추가

    # 인구 이동
    for i, j in united:
        A[i][j] = summary // count

    return count

# 더 이상 인구 이동이 불가능할 때 까지 반복
while True:
    union = [[-1] * n for _ in range(n)]
    index = 0 # 연합 번호
    for i in range(n):
        for j in range(n):
            # 해당 국가에 대한 연합이 아직 확인되지 않은 경우
            if union[i][j] == -1:
                bfs(i, j, index)
                index += 1

    # 모든 인구이동 종료
    if index == n * n:
        break
    
    answer += 1

print(answer)