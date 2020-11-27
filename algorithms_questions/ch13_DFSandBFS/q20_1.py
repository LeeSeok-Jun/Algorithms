"""
감시 피하기 - 2회차
"""

# 풀이 제한 시간 : 60분
# 2020/11/27 12:24 ~ 12:53
# 회전이 바뀔 때, nr과 nc의 위치를 처음 위치로 해야 한다.
# 함수가 실행 될때만 nr과 nc의 위치를 고정하면 다음 회전에서 인덱스가 이상하게 지정된다!

n = int(input())

graph = []
answer = 'NO'
num_of_teacher = 0

for i in range(n):
    graph.append(input().split())

    for j in range(n):
        if graph[i][j] == 'T':
            num_of_teacher += 1

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def watch(r, c):
    # nr = r
    # nc = c

    for i in range(4):
        nr = r
        nc = c

        while(True):
            nr += dr[i]
            nc += dc[i]

            if nr >= 0 and nr < n and nc >= 0 and nc < n:
                if graph[nr][nc] == 'S':
                    return False
                elif graph[nr][nc] == 'O':
                    break
            else:
                break

    return True

def dfs(count):
    global answer

    if count == 3:
        num_of_true = 0

        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'T':
                    if watch(i, j):
                        num_of_true += 1

        if num_of_true == num_of_teacher:
            answer = 'YES'

    else:
        for i in range(n):
            for j in range(n):
                if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    count += 1

                    dfs(count)

                    count -= 1
                    graph[i][j] = 'X'

dfs(0)
print(answer)