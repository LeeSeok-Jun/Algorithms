"""
자물쇠외 열쇠 - 2회차
"""

# 2020/11/12 11:29 A.M. ~ 12:20 P.M. (50분)
# 풀이는 맞았으나 풀이 제한 시간(40분) 초과

def rotate_key(key):
    n = len(key)
    rotated_key = [[0] * (n) for _ in range(n)]

    for i in range(n):
        for j in range((n)):
            rotated_key[j][n-1-i] = key[i][j]

    return rotated_key

def check_lock(new_lock):

    n = int(len(new_lock) / 3)

    for i in range(n, 2*n):
        for j in range(n, 2*n):
            if new_lock[i][j] != 1:
                return False
    
    return True
    

def solution(key, lock):
    import pprint

    new_lock = [[0] * (3 * len(lock)) for _ in range(3 * len(lock))]

    for i in range(len(lock)):
        for j in range(len(lock)):
            new_lock[i + len(lock)][j + len(lock)] = lock[i][j] 

    for _ in range(4):
        key = rotate_key(key)

        for i in range(len(new_lock)-len(lock)+1):
            for j in range(len(new_lock)-len(lock)+1):

                for r in range(len(key)):
                    for c in range(len(key)):
                        new_lock[i+r][j+c] += key[r][c]

                if check_lock(new_lock):
                    return True
                else:
                    for r in range(len(key)):
                        for c in range(len(key)):
                            new_lock[i+r][j+c] -= key[r][c]


    return False

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))