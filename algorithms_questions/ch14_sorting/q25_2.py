"""
실패율 - 3회차
"""

# 풀이 제한 시간 : 20분
# 2021/01/21 14:34 ~ 14:56
# 실패 - 정답이긴 하지만 시간 초과

def solution(n, stages):
    answer = []
    rest_user = len(stages)
    failure_ratio = []

    for i in range(1, n+1):
        failure_user = 0

        for st in stages:
            if st == i:
                failure_user += 1
        
        if rest_user == 0:
            failure_ratio.append((0, i))
        else:
            failure_ratio.append((failure_user / rest_user, i))
            rest_user -= failure_user
    
    failure_ratio.sort(key = lambda x: (-x[0], x[1]))
    for fr in failure_ratio:
        answer.append(fr[1])

    return answer