"""
자물쇠와 열쇠 - 3회차
"""

# 풀이 제한 시간 : 40분
# 2021/01/14 13:12 ~ 14:02
# 실패 - 틀린부분 주석 처리

def check_lock(new_lock):
    n = int(len(new_lock)/3)

    # for i in range(len(new_lock), 2*len(new_lock)):
    #     for j in range(len(new_lock), 2*len(new_lock)):
    #         if new_lock[i][j] != 1:
    #             return False
    # return True

    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if new_lock[i][j] != 1:
                return False
    return True

def rotate_key(key):
    m = len(key)
    new_key = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            # new_key[j][m-i] = key[i][j]
            new_key[j][m-1-i] = key[i][j]
    return new_key

def solution(key, lock):
    n = len(lock)
    m = len(key)

    new_lock = [[0] * (3*n) for _ in range(3*n)]
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
            
    for _ in range(4):
        key = rotate_key(key)

        for i in range(2*n+1):
            for j in range(2*n+1):

                for r in range(m):
                    for c in range(m):
                        new_lock[i+r][j+c] += key[r][c]
                        # new_lock[i+m][j+m] += key[r][c]

                if check_lock(new_lock):
                    return True
                else:
                    for r in range(m):
                        for c in range(m):
                            # new_lock[i+m][j+m] -= key[r][c]
                            new_lock[i+r][j+c] -= key[r][c]

    return False