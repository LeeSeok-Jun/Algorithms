"""
괄호 변환 - 2회차
"""

# 풀이 제한 시간 : 20분
# 2020/11/26 12:45 ~

def isBalanced(w):
    count = 0

    for i in w:
        if i == '(':
            count += 1
        else:
            count -= 1

    if count == 0:
        return True
    else:
        return False
    
def isCorrect(w):
    count = 0

    for i in w:
        if i == '(':
            count += 1
        else:
            count -= 1

            if count == -1:
                return False
    
    return True


def solution(p):

    if p == '':
        return ''

    # 범위 조심 : p[:i+1]은 0부터 i번까지의 인덱스에 해당하는 문자열을 의미!
    for i in range(len(p)):
        if isBalanced(p[:i+1]):
            u = p[:i+1]
            v = p[i+1:]
            break
    
    if isCorrect(u):
        answer = u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        for i in range(1, len(u)-1):
            if u[i] == '(':
                answer += ')'
            else:
                answer += '('

    return answer