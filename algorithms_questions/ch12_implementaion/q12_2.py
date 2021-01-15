"""
기둥과 보 설치 - 3회차
"""

# 풀이 제한 시간 : 50분
# 2021/01/15 13:50 ~ 14:45
# 시간 초과 - 틀린 부분 주석 처리

def check_build(building):
    for b in building:
        x, y, a = b
        if a == 0:
            if y != 0:
                
                # if [x, y-1, 0] not in building and [x-1, y-1, 1] not in building: 
                #     return False

                if [x, y-1, 0] not in building and [x-1, y, 1] not in building and [x, y, 1] not in building:
                    return False

        else:
            if [x, y-1, 0] not in building and [x+1, y-1, 0] not in building:
                if [x-1, y, 1] not in building or [x+1, y, 1] not in building:
                    return False
    return True

def solution(n, build_frame):
    answer = []

    for bf in build_frame:
        x, y, a, b = bf
        if b == 1:
            answer.append([x, y, a])
            if not check_build(answer):
                answer.remove([x, y, a])
        else:
            if [x, y, a] in answer:
                answer.remove([x, y, a])
                if not check_build(answer):
                    answer.append([x, y, a])

    # answer.sort()
    # return answer

    return sorted(answer)

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
print(solution(n, build_frame))