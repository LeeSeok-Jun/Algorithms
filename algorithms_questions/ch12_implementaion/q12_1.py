"""
기둥과 보 설치 - 2회차
"""

# 2020/11/13 10:56 A.M. ~ 11:34 A.M.
# 정답!

def possible(n, answer):
    for i in answer:
        x, y, a = i

        if x > n or x < 0 or y > n or y < 0:
            return False

        # 기둥
        if a == 0:
            if y == 0:
                continue
            elif ([x, y-1, 0] not in answer) and ([x-1, y, 1] not in answer) and ([x, y, 1] not in answer):
                return False

        # 보
        else:
            if ([x, y-1, 0] not in answer) and ([x+1, y-1, 0] not in answer) and (([x-1, y, 1] not in answer) or ([x+1, y, 1] not in answer)):
                return False

    return True

def solution(n, build_frame):
    answer = []

    for frame in build_frame:
        x, y, a, b = frame

        # Delete
        if b == 0:
            answer.remove([x,y,a])

            if possible(n, answer):
                continue
            else:
                answer.append([x,y,a])

        # Install
        else:
            answer.append([x,y,a])

            if possible(n, answer):
                continue
            else:
                answer.remove([x,y,a])
    
    return sorted(answer)


n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(5, build_frame))