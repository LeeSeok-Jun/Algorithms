"""
연구소 - 해설
"""

n, m = map(int, input().split())
data = [] # 초기 연구소
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤 연구소

# 연구소 초기화
for _ in range(n):
    data.append(list(map(int, input().split())))

# 4가지 방향 이동에 대한 리스트
dr = [-1, 0, 1, 0] # 상하 이동
dc = [0, 1, 0, -1] # 좌우 이동

result = 0

# DFS를 이용하여 바이러스의 전파 구현
def virus(r, c):
    # 4가지 방향에 대해서
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 바이러스가 퍼질 수 있는 경우
        if nr >= 0 and nr < n and nc >= 0 and nc < m:
            if temp[nr][nc] == 0:
                # 해당 위치에 바이러스를 전파하고 재귀적으로 진행
                temp[nr][nc] = 2
                virus(nr, nc)

# 안전 구역의 크기를 계산하는 함수
def getScore():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1

    return score

# DFS를 이용하여 울타리를 설치하면서 매번 안전 영역의 크기 계산
# count : 새로 설치된 울타리의 수
def dfs(count):
    global result

    # 울타리 3개가 모두 설치된 경우
    if count == 3:
        # 바이러스 전파 시뮬레이션을 위해 그래프 복사
        for i in range(n):
            for j in range(m):
                temp[i][j] = data[i][j]

        # 각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)

        # 안전 영역의 최댓값 계산
        result = max(result, getScore())
        return
    
    # 울타리 설치
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                data[i][j] = 1 # 빈 공간에 울타리 설치
                count += 1 # 설치한 울타리 수 증가

                dfs(count) # dfs 진행
                # 만약 count가 3보다 작다면 다른 위치에 새롭게 울타리 설치를 진행할 것이다.
                
                # 만약 count가 3이 되었다면 스코어를 계산하고 설치했던 울타리를 다시 제거할 것이다.
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)