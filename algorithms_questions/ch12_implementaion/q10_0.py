"""
자물쇠와 열쇠
- https://programmers.co.kr/learn/courses/30/lessons/60059
- 자물쇠는 격자 한 칸의 크기가 1 * 1인 N * N 크기의 정사각 격자 형태이다.
- 열쇠는 M * M 크기인 정사각 격자 형태로 되어 있다.
- 자물쇠와 열쇠는 둘 다 돌기와 홈을 가지고 있다.
- 열쇠는 회전과 이동이 가능하며 열쇠의 돌기 부분을 자물쇠의 홈 부분에 딱 맞게 채우면 자물쇠가 열리는 구조이다.
- 자물쇠의 돌기와 열쇠의 돌기가 만나서는 안 된다.
- 자물쇠의 모든 홈을 채워 비어있는 곳이 없어야 자물쇠를 열 수 있다.
- 열쇠를 나타내는 2차원 배열 key와 자물쇠를 나타내는 2차원 배열 lock이 매개변수로 주어질 때,
  열쇠를 자물쇠로 열 수 있으면 true를 그렇지 않다면 false를 return 하도록 solution 함수를 완성하시오.
"""

# 2020/11/05 03:42 P.M. ~ 시간 초과
# 실패 - 문제 접근 방법은 맞추었으나 구현능력 부족으로 인해 실패함

# 2차원 리스트를 90도 회전하는 함수
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이(세로)
    m = len(a[0]) # 열 길이(가로)

    result = [[0] * n for _ in range(m)] # 회전 결과를 담을 리스트

    # 시계방향으로 90회전
    # result의 우상단부터 아래로 내려가면서 채운다고 생각하면 이해하기 쉬움.
    # j가 커지면서 result의 행은 아래로 내려가고
    # i가 커지면서 result의 열은 오른족에서 왼쪽으로 이동하는 형태를 보인다.
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = a[i][j] 

    return result

# 자물쇠 검사
def check(new_lock):
    lock_length = len(new_lock) // 3

    # 기존의 3배 크기로 늘린 자물쇠는 중앙 부분이 기존 자물쇠의 형태를 갖는다.
    # 중앙 부분의 원소들의 모든 값이 1이 된다면 자물쇠는 풀린 것으로 간주할 수 있다.
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if new_lock[i][j] != 1:
                return False
    
    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)

    # 자물쇠의 크기를 기존의 3배로 변환
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]

    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]

    # 키를 총 4번 회전하면서 새로운 자물쇠에 대해 완전 탐색 진행
    for _ in range(4):
        key = rotate_a_matrix_by_90_degree(key) # 90도 회전

        # 새로운 자물쇠에 대해서
        # x, y는 새로운 자물쇠의 인덱스를 의미힌다.
        for x in range(n * 2):
            for y in range(n * 2):
                # 열쇠를 자물쇠에 끼어넣기
                # i, j는 열쇠의 인덱스를 위치한다.
                # 결과적으로 x+i, y+j는 자물쇠 내의 열쇠 위치를 의미힌다.
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]

                # 지물쇠가 열리는지 검사
                if check(new_lock) == True:
                    return True

                # 자물쇠에서 열쇠 제거
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]

    return False