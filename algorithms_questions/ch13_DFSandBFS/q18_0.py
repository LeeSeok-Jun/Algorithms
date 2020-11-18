"""
괄호 변환
- https://programmers.co.kr/learn/courses/30/lessons/60058
"""

# 2020/11/18 11:20 A.M. ~
# 실패

def balanced_index(p):
    count = 0
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1

        if count == 0:
            return i

def check_proper(p):
    count = 0

    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 다음 문자로 ')'이 나왔는데 이미 count가 0이면 올바르지 않은 문자열
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    if p == '':
        return answer

    # 두 개의 균형잡인 문자열로 분리
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]

    if check_proper(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫번째와 마지막 문자 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        
        answer += ''.join(u)
    return answer