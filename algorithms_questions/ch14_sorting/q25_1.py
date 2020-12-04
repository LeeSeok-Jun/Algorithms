"""
실패율 - 2회차
"""

# 풀이 제한 시간 : 20분
# 2020/12/04 11:10 ~ 11:18
# 성공

def solution(N, stages):
    people = len(stages)
    answer = []
    data = []

    for i in range(1, N+1):
        failure = 0
        num = 0

        for stage in stages:
            if stage == i:
                num += 1
        
        if people <= 0:
            failure = 0
        else:
            failure = num / people

        data.append((i, failure))
        people -= num
        
    data.sort(key = lambda x : -x[1])
    for d in data:
        answer.append(d[0])

    return answer